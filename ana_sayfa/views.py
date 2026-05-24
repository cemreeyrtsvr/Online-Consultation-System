from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Uzman, Danisan, Randevu, Mesaj, Musaitlik, Yorum
from django.http import JsonResponse
from django.db.models import Q, Avg
from decimal import Decimal

# --- 1. GİRİŞ & KAYIT SİSTEMİ ---
def giris_sayfasi(request):
    return render(request, 'index.html')

def kayit_ol(request, rol):
    hata = None
    if request.method == 'POST':
        u_name = request.POST.get('u_name', '').strip()
        ad = request.POST.get('ad', '').strip()
        soyad = request.POST.get('soyad', '').strip()
        email = request.POST.get('email', '').strip().lower()
        sifre = request.POST.get('sifre')

        if " " in u_name:
            hata = "Kullanıcı adında boşluk olamaz!"
        elif User.objects.filter(username=u_name).exists():
            hata = "Bu kullanıcı adı zaten alınmış!"
        elif User.objects.filter(email=email).exists():
            hata = "Bu e-posta adresi zaten kullanımda!"
        elif rol == 'uzman':
            anahtar = request.POST.get('uzman_anahtar')
            if anahtar != "uzman2026":
                hata = "Geçersiz uzmanlık anahtarı!"

        if hata:
            return render(request, 'kayit.html', {'rol': rol, 'hata': hata})

        yeni_user = User.objects.create_user(
            username=u_name, password=sifre, email=email,
            first_name=ad, last_name=soyad
        )

        if rol == 'ogrenci':
            Danisan.objects.create(user=yeni_user)
            login(request, yeni_user)
            return redirect('ana_sayfa')
        else:
            brans = request.POST.get('brans', 'psikolog')
            Uzman.objects.create(
                user=yeni_user, ad_soyad=f"{ad} {soyad}",
                brans=brans, unvan="Uzman Danışman",
                resim_emoji="👨‍⚕️"
            )
            login(request, yeni_user)
            return redirect('profil_sayfasi')
    return render(request, 'kayit.html', {'rol': rol})

def login_sayfasi(request, rol):
    hata = None
    if request.method == 'POST':
        u_name = request.POST.get('username')
        sifre = request.POST.get('password')
        user = authenticate(request, username=u_name, password=sifre)
        if user is not None:
            login(request, user)
            return redirect('ana_sayfa' if hasattr(user, 'danisan') else 'profil_sayfasi')
        else:
            hata = "Kullanıcı adı veya şifre hatalı!"
    rol_gosterimi = "Öğrenci" if rol == 'ogrenci' else "Danışman"
    return render(request, 'login.html', {'rol': rol, 'rol_gosterimi': rol_gosterimi, 'hata': hata})

# --- 2. PROFİL YÖNETİMİ ---
@login_required
def profil_sayfasi(request):
    user = request.user
    is_uzman = hasattr(user, 'uzman')
    profil_obj = user.uzman if is_uzman else user.danisan

    if is_uzman:
        yaklasan = Randevu.objects.filter(uzman__user=user)
        # UZMAN İÇİN: Kendisine gelen tüm benzersiz sohbet odalarını bul
        # oda_adi formatımız: oda_admin_danisanadi
        aktif_sohbetler = Mesaj.objects.filter(oda__contains=user.username).values('oda').distinct()
    else:
        yaklasan = Randevu.objects.filter(danisan__user=user)
        # DANIŞAN İÇİN: Kendi mesajlarını ve uzmanlarını listele
        aktif_sohbetler = Mesaj.objects.filter(oda__contains=user.username).values('oda').distinct()

    kullanici_verisi = {
        'ad_soyad': f"{user.first_name} {user.last_name}",
        'email': user.email,
        'kayit_tarihi': user.date_joined.strftime("%B %Y"),
        'ilk_harf': user.first_name[0].upper() if user.first_name else "U",
        'telefon': getattr(profil_obj, 'telefon', 'Belirtilmedi'),
        'foto': profil_obj.profil_resmi.url if profil_obj.profil_resmi else None,
        'bakiye': getattr(profil_obj, 'bakiye', 0)
    }

    return render(request, 'profil.html', {
        'kullanici': kullanici_verisi,
        'yaklasan_randevular': yaklasan,
        'is_uzman': is_uzman,
        'aktif_sohbetler': aktif_sohbetler # Burası önemli!
    })

@login_required
def profil_duzenle(request):
    user = request.user
    profil = user.uzman if hasattr(user, 'uzman') else user.danisan
    if request.method == 'POST':
        user.first_name = request.POST.get('ad')
        user.last_name = request.POST.get('soyad')
        user.email = request.POST.get('email')
        yeni_sifre = request.POST.get('sifre')
        if yeni_sifre and yeni_sifre.strip() != "":
            user.set_password(yeni_sifre)
            update_session_auth_hash(request, user)
        user.save()
        if request.FILES.get('profil_foto'):
            profil.profil_resmi = request.FILES.get('profil_foto')
        if hasattr(user, 'danisan'):
            profil.telefon = request.POST.get('telefon')
        profil.save()
        return redirect('profil_sayfasi')
    return render(request, 'profil_duzenle.html', {'profil': profil})

# --- 3. ANA SAYFA & ARAMA MOTORU ---
def ana_sayfa(request):
    query = request.GET.get('q')
    uzmanlar = None
    if query:
        uzmanlar = Uzman.objects.filter(
            Q(ad_soyad__icontains=query) | Q(brans__icontains=query),
            aktif_mi=True
        )
    toplam_uzman = Uzman.objects.filter(aktif_mi=True).count()
    return render(request, 'home.html', {'uzmanlar': uzmanlar, 'query': query, 'toplam_uzman': toplam_uzman})

def bolum_detay(request, bolum_adi):
    uzmanlar = Uzman.objects.filter(brans=bolum_adi, aktif_mi=True).annotate(ortalama_puan=Avg('yorumlar__puan'))
    return render(request, 'bolum.html', {'doktorlar': uzmanlar, 'bolum_adi': bolum_adi.title()})

# --- 4. UZMAN & DANIŞAN SEANS YÖNETİMİ ---
@login_required
def uzman_saat_ekle(request):
    if not hasattr(request.user, 'uzman'):
        return redirect('ana_sayfa')
    if request.method == 'POST':
        tarih = request.POST.get('tarih')
        saatler = request.POST.getlist('saatler')
        for s in saatler:
            Musaitlik.objects.get_or_create(uzman=request.user.uzman, gun=tarih, saat=s)
        return redirect('profil_sayfasi')
    return render(request, 'uzman_saat_ekle.html')

@login_required
def randevu_saat_sec(request, uzman_id):
    uzman = get_object_or_404(Uzman, id=uzman_id)
    danisan = get_object_or_404(Danisan, user=request.user)
    bos_saatler = Musaitlik.objects.filter(uzman=uzman, dolu_mu=False).order_by('gun', 'saat')
    if request.method == 'POST':
        saat_id = request.POST.get('saat_id')
        odeme_turu = request.POST.get('odeme_turu')
        if odeme_turu == 'cuzdan':
            return redirect('cuzdanla_ode', saat_id=saat_id)
        return redirect('odeme_yap', saat_id=saat_id)
    return render(request, 'saat_secimi.html', {'uzman': uzman, 'bos_saatler': bos_saatler, 'bakiye': danisan.bakiye})

@login_required
def odeme_yap(request, saat_id):
    saat = get_object_or_404(Musaitlik, id=saat_id)
    danisan_obj = get_object_or_404(Danisan, user=request.user)
    if request.method == 'POST':
        Randevu.objects.create(danisan=danisan_obj, uzman=saat.uzman, tarih=saat.gun, saat=saat.saat, durum='beklemede', alinan_ucret=saat.uzman.ucret, odeme_alindi=True)
        saat.dolu_mu = True
        saat.save()
        return redirect('profil_sayfasi')
    return render(request, 'odeme.html', {'saat': saat, 'ucret': saat.uzman.ucret})

# --- 5. CÜZDAN İŞLEMLERİ ---
@login_required
def bakiye_yukle(request):
    danisan = get_object_or_404(Danisan, user=request.user)
    if request.method == 'POST':
        miktar = request.POST.get('miktar')
        if miktar:
            danisan.bakiye += Decimal(miktar)
            danisan.save()
            return redirect('profil_sayfasi')
    return render(request, 'bakiye_yukle.html')

@login_required
def cuzdanla_ode(request, saat_id):
    saat = get_object_or_404(Musaitlik, id=saat_id)
    danisan = get_object_or_404(Danisan, user=request.user)
    ucret = saat.uzman.ucret
    if danisan.bakiye >= ucret:
        danisan.bakiye -= ucret
        danisan.save()
        Randevu.objects.create(danisan=danisan, uzman=saat.uzman, tarih=saat.gun, saat=saat.saat, alinan_ucret=ucret, durum='beklemede', odeme_alindi=True)
        saat.dolu_mu = True
        saat.save()
        return redirect('profil_sayfasi')
    return redirect('bakiye_yukle')

# --- 6. ONAY / RED & İADE İŞLEMLERİ ---
@login_required
def randevu_onayla(request, randevu_id):
    randevu = get_object_or_404(Randevu, id=randevu_id, uzman__user=request.user)
    if randevu.durum == 'beklemede':
        randevu.durum = 'onaylandi'
        randevu.save()
        uzman = randevu.uzman
        uzman.bakiye += randevu.alinan_ucret
        uzman.save()
    return redirect('profil_sayfasi')

@login_required
def randevu_reddet(request, randevu_id):
    randevu = get_object_or_404(Randevu, id=randevu_id, uzman__user=request.user)
    if randevu.durum == 'beklemede':
        danisan = randevu.danisan
        danisan.bakiye += randevu.alinan_ucret
        danisan.save()
        randevu.durum = 'reddedildi'
        randevu.save()
        musaitlik = Musaitlik.objects.filter(uzman=randevu.uzman, gun=randevu.tarih, saat=randevu.saat).first()
        if musaitlik:
            musaitlik.dolu_mu = False
            musaitlik.save()
    return redirect('profil_sayfasi')

# --- 7. YORUM & PUANLAMA ---
@login_required
def yorum_ekle(request, uzman_id):
    if request.method == "POST":
        uzman = get_object_or_404(Uzman, id=uzman_id)
        danisan = get_object_or_404(Danisan, user=request.user)
        puan = request.POST.get('puan')
        icerik = request.POST.get('icerik')
        if puan and icerik:
            Yorum.objects.create(uzman=uzman, danisan=danisan, puan=int(puan), icerik=icerik)
        return redirect('bolum_detay', bolum_adi=uzman.brans)
    return redirect('ana_sayfa')

# --- 8. MESAJLAŞMA & CHAT ---
@login_required
def chat_odasi(request, oda_adi):
    # Oda adı eşleşmesini sağlamak için küçük harfe çevirebilirsin ama standart 'oda_admin_kullanici' ise buna gerek yok
    if request.method == "POST":
        icerik = request.POST.get('mesaj')
        if icerik:
            # OKUNDU hatasını çözmek için Mesaj modeline alan eklediğini varsayıyoruz
            Mesaj.objects.create(
                oda=oda_adi,
                gonderen=request.user.username,
                icerik=icerik,
                okundu=False
            )
        return redirect('chat_odasi', oda_adi=oda_adi)

    # Odaya girince gelen mesajları okundu yapıyoruz
    Mesaj.objects.filter(oda=oda_adi).exclude(gonderen=request.user.username).update(okundu=True)

    mesajlar = Mesaj.objects.filter(oda=oda_adi).order_by('tarih')
    return render(request, 'chat.html', {'mesajlar': mesajlar, 'oda_adi': oda_adi})

def logout(request):
    auth_logout(request)
    return redirect('giris_sayfasi')

def danisan_sayfasi(request):
    return render(request, 'danisan.html')

def odeme_sayfasi(request):
    return render(request, 'odeme.html')