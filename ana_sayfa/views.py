from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mesaj
import random


def giris_sayfasi(request):
    return render(request, 'index.html')


def login_sayfasi(request, rol):
    if request.method == 'POST':
        if rol == 'ogrenci':
            return redirect('ana_sayfa')
        elif rol == 'danisan':
            return redirect('danisan_sayfasi')

    rol_gosterimi = "Öğrenci" if rol == 'ogrenci' else "Danışman / Uzman"
    return render(request, 'login.html', {'rol': rol, 'rol_gosterimi': rol_gosterimi})


def ana_sayfa(request):
    return render(request, 'home.html')


def bolum_detay(request, bolum_adi):
    basliklar = {
        'diyetisyen': 'Beslenme ve Diyet Uzmanları',
        'psikolog': 'Online Psikolog & Terapi',
        'fizyoterapi': 'Fizyoterapi ve Rehabilitasyon',
    }

    yorumlar_havuzu = [
        {'ad': 'Elif K.', 'puan': 5,
         'yorum': 'Hocamız çok ilgili, sürecim harika ilerliyor. Kesinlikle tavsiye ederim.'},
        {'ad': 'Murat T.', 'puan': 5, 'yorum': 'İlk seanstan itibaren farkı hissettim. Enerjisi çok yüksek.'},
        {'ad': 'Selin A.', 'puan': 4,
         'yorum': 'Çok bilgili bir uzman, sadece randevu saatlerinde bazen yoğunluk oluyor.'},
        {'ad': 'Ahmet Y.', 'puan': 5, 'yorum': 'Hayatımı değiştirdi diyebilirim. Teşekkürler hocam!'},
        {'ad': 'Canan B.', 'puan': 5, 'yorum': 'Detaylı açıklamaları ve güler yüzü ile çok memnun kaldım.'},
    ]

    tum_doktorlar = {
        'diyetisyen': [
            {
                'id': 'dyt-ayse',
                'ad': 'Uzm. Dyt. Ayşe Yılmaz',
                'resim': '👩‍⚕️',
                'unvan': 'Klinik Beslenme Uzmanı',
                'puan': 4.9,
                'danisan_sayisi': 1240,
                'deneyim': '12 Yıl',
                'kisa_ozet': 'Sürdürülebilir beslenme ve metabolizma hastalıkları uzmanı.',
                'uzun_bilgi': """Hacettepe Üniversitesi Beslenme ve Diyetetik bölümünden 2012 yılında onur derecesiyle mezun oldum. Ardından İngiltere'de "Metabolik Sendrom ve Beslenme" üzerine yüksek lisansımı tamamladım. 

12 yıllık meslek hayatımda 1000'den fazla danışanla birebir çalışma fırsatı buldum. Benim felsefem "Diyet yapmak değil, yaşam tarzını değiştirmek" üzerine kuruludur. Yasaklarla dolu listeler yerine, sevdiğiniz yiyecekleri porsiyon kontrolüyle hayatınıza entegre etmeyi öğretiyorum.

Özellikle İnsülin Direnci, Haşimato ve Polikistik Over Sendromu (PKOS) beslenmesi konularında uzmanlaştım. Sizi de bu sağlıklı yolculuğa bekliyorum.""",
                'alanlar': ['Kilo Yönetimi', 'Diyabet', 'Hamilelik', 'Vegan Beslenme'],
                'yorumlar': random.sample(yorumlar_havuzu, 3)
            },
            {
                'id': 'dyt-mehmet',
                'ad': 'Dyt. Mehmet Demir',
                'resim': '👨‍⚕️',
                'unvan': 'Sporcu Beslenmesi Uzmanı',
                'puan': 4.7,
                'danisan_sayisi': 850,
                'deneyim': '6 Yıl',
                'kisa_ozet': 'Profesyonel sporcular ve kas kazanımı odaklı beslenme.',
                'uzun_bilgi': """Spor bilimleri ve beslenme disiplinlerini birleştirerek, sporcuların performansını maksimize etmeyi hedefliyorum. Milli takım seviyesindeki sporculardan, hobi amaçlı fitness yapan bireylere kadar geniş bir yelpazede danışmanlık veriyorum.

Kas kütlesini artırmak, yağ oranını düşürmek veya maraton/triatlon gibi yarışlara hazırlanmak istiyorsanız doğru yerdesiniz. Kulaktan dolma bilgiler yerine, tamamen supplement (takviye) kullanımı konusunda bilimsel ve kanıta dayalı rehberlik sunuyorum.""",
                'alanlar': ['Sporcu Beslenmesi', 'Supplement', 'Kilo Alma', 'Performans'],
                'yorumlar': random.sample(yorumlar_havuzu, 3)
            },
        ],
        'psikolog': [
            {
                'id': 'psk-zeynep',
                'ad': 'Uzm. Psk. Zeynep Kaya',
                'resim': '👩‍⚕️',
                'unvan': 'Klinik Psikolog',
                'puan': 5.0,
                'danisan_sayisi': 2100,
                'deneyim': '15 Yıl',
                'kisa_ozet': 'Bilişsel Davranışçı Terapi (BDT) ve EMDR uygulayıcısı.',
                'uzun_bilgi': """Boğaziçi Üniversitesi Psikoloji bölümü mezunuyum. Klinik Psikoloji yüksek lisansımı Hollanda'da tamamladım. 15 yıldır aktif olarak danışan görüyorum. Uzmanlık alanım Kaygı Bozuklukları (Anksiyete) ve Depresyon.

Terapi sürecinde "Bilişsel Davranışçı Terapi" (BDT) ekolünü benimsiyorum. Düşünce, duygu ve davranış arasındaki döngüyü fark etmenizi ve bunu kendi başınıza yönetmenizi sağlıyorum. Ayrıca derin travma çalışmaları için uluslararası geçerliliğe sahip EMDR sertifikasına sahibim. Güvenli bir alanda, yargılanmadan dinlenmek isterseniz seanslarımıza katılabilirsiniz.""",
                'alanlar': ['Anksiyete', 'Depresyon', 'İlişki Terapisi', 'EMDR'],
                'yorumlar': random.sample(yorumlar_havuzu, 4)
            },
        ],
        'fizyoterapi': [
            {
                'id': 'fzt-can',
                'ad': 'Fzt. Can Yılmaz',
                'resim': '👨‍⚕️',
                'unvan': 'Manuel Terapist',
                'puan': 4.8,
                'danisan_sayisi': 750,
                'deneyim': '7 Yıl',
                'kisa_ozet': 'Bel, boyun fıtığı ve duruş bozuklukları.',
                'uzun_bilgi': """Fizik tedavi sürecini sadece sıradan egzersizlerle değil, kişiye özel manuel terapi teknikleriyle destekliyorum. Özellikle masa başı çalışanlarda çok sık görülen boyun düzleşmesi, sırt ağrıları ve bel fıtığı konularında uzmanlaştım.

Benim klinik yaklaşımımda amaç sadece geçici olarak ağrıyı dindirmek değil, ağrının gerçek kaynağını bulup tekrarlamasını engellemektir. Seanslarımız sonrasında size özel hazırladığım video destekli ev egzersiz programlarıyla iyileşme sürecinizi hızlandırıyoruz.""",
                'alanlar': ['Bel Fıtığı', 'Boyun Ağrısı', 'Manuel Terapi', 'Duruş Bozukluğu'],
                'yorumlar': random.sample(yorumlar_havuzu, 3)
            },
        ]
    }

    secilen_doktorlar = tum_doktorlar.get(bolum_adi, [])
    context = {'bolum_adi': bolum_adi, 'baslik': basliklar.get(bolum_adi, 'Uzmanlar Listesi'),
               'doktorlar': secilen_doktorlar}
    return render(request, 'bolum.html', context)


def odeme_sayfasi(request):
    doktor_adi = request.GET.get('doktor', 'Uzman Doktor')
    tarih = request.GET.get('tarih', 'Belirtilmedi')
    saat = request.GET.get('saat', 'Belirtilmedi')
    context = {'doktor_adi': doktor_adi, 'tarih': tarih, 'saat': saat, 'fiyat': '1.250 TL'}
    return render(request, 'odeme.html', context)


def profil_sayfasi(request):
    context = {
        'kullanici': {'ad_soyad': 'Test Öğrencisi', 'email': 'ogrenci@test.com', 'telefon': '+90 555 123 45 67',
                      'kayit_tarihi': 'Eylül 2025'},
        'yaklasan_randevular': [
            {'doktor': 'Uzm. Dyt. Ayşe Yılmaz', 'bolum': 'Klinik Beslenme', 'tarih': '25 Şubat 2026', 'saat': '14:00',
             'durum': 'Onaylandı', 'durum_renk': '#27ae60'}],
        'gecmis_randevular': [
            {'doktor': 'Psk. Kemal Öztürk', 'bolum': 'Psikoterapist', 'tarih': '10 Ocak 2026', 'saat': '11:00',
             'durum': 'Tamamlandı', 'durum_renk': '#3498db'}]
    }
    return render(request, 'profil.html', context)


def danisan_sayfasi(request):
    context = {
        'uzman': {
            'id': 'dyt-ayse',
            'ad_soyad': 'Uzm. Dyt. Ayşe Yılmaz',
            'unvan': 'Klinik Beslenme Uzmanı',
            'puan': 4.9,
            'bakiye': '14.500 TL',
            'aylik_kazanc': '32.400 TL',
            'toplam_danisan': 1240
        },
        'bekleyen_talepler': [
            {'danisan_ad': 'Elif Koç', 'tarih': '22 Şubat 2026', 'saat': '11:00', 'hizmet': 'İlk Görüşme'},
            {'danisan_ad': 'Canan B.', 'tarih': '22 Şubat 2026', 'saat': '15:30', 'hizmet': 'Kontrol Seansı'}
        ],
        'bugunku_randevular': [
            {
                'id': 'dyt-ayse', 'danisan_ad': 'Ahmet Demir', 'saat': '14:00',
                'durum': 'Yaklaşıyor', 'durum_renk': '#f39c12',
                'not': 'Kilo verme süreci, 2. seans. Kan tahlili yüklendi.'
            },
            {
                'id': 'dyt-ayse', 'danisan_ad': 'Zeynep Kaya', 'saat': '16:30',
                'durum': 'Onaylandı', 'durum_renk': '#27ae60', 'not': 'Diyabet ve beslenme listesi güncellemesi.'
            }
        ],
        'son_yorumlar': [
            {'danisan': 'Selin A.', 'puan': 5,
             'yorum': 'Harika bir seanstı, motivasyonum çok arttı! Listeler hiç zorlamıyor.'},
            {'danisan': 'Ahmet Y.', 'puan': 5, 'yorum': 'Güler yüzlü ve çok ilgili bir uzman. Teşekkürler.'}
        ]
    }
    return render(request, 'danisan.html', context)


@csrf_exempt
def mesaj_gonder(request):
    if request.method == 'POST':
        oda = request.POST.get('oda')
        yazi = request.POST.get('mesaj', '')
        dosya = request.FILES.get('dosya')
        gonderen = request.POST.get('gonderen', 'Kullanıcı')
        if oda:
            Mesaj.objects.create(oda=oda, gonderen=gonderen, icerik=yazi, dosya=dosya)
            return JsonResponse({'durum': 'basarili'})
    return JsonResponse({'durum': 'hata'})


def mesajlari_getir(request):
    oda = request.GET.get('oda')
    if oda:
        mesajlar = Mesaj.objects.filter(oda=oda).order_by('tarih')
    else:
        mesajlar = []

    data = []
    for m in mesajlar:
        dosya_url = m.dosya.url if m.dosya else None
        zaman = m.tarih.strftime("%H:%M")
        data.append({'gonderen': m.gonderen, 'icerik': m.icerik, 'dosya_url': dosya_url,
                     'dosya_adi': m.dosya.name.split('/')[-1] if m.dosya else 'Dosya', 'zaman': zaman})
    return JsonResponse({'mesajlar': data})