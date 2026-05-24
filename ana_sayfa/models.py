from django.db import models
from django.contrib.auth.models import User

# 1. Uzman Profili
class Uzman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ad_soyad = models.CharField(max_length=150)
    unvan = models.CharField(max_length=150)
    brans = models.CharField(max_length=50, choices=[
        ('diyetisyen', 'Diyetisyen'),
        ('psikolog', 'Psikolog'),
        ('fizyoterapi', 'Fizyoterapi')
    ])
    resim_emoji = models.CharField(max_length=10, default="👨‍⚕️")
    profil_resmi = models.ImageField(upload_to='profiller/', blank=True, null=True)
    biyografi = models.TextField()
    ucret = models.DecimalField(max_digits=10, decimal_places=2, default=1250.00)
    # Bakiye burada olmalı!
    bakiye = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    puan = models.FloatField(default=5.0)
    aktif_mi = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.unvan} {self.ad_soyad}"

# 2. Danışan Profili (Öğrenci)
class Danisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    tc_no = models.CharField(max_length=11, blank=True, null=True)
    profil_resmi = models.ImageField(upload_to='profiller/', blank=True, null=True)
    bakiye = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.get_full_name()

# 3. Randevular
class Randevu(models.Model):
    DURUM_CHOICES = [
        ('beklemede', 'Onay Bekliyor'),
        ('onaylandi', 'Onaylandı'),
        ('reddedildi', 'Reddedildi / İade Edildi'),
    ]

    uzman = models.ForeignKey(Uzman, on_delete=models.CASCADE, related_name='randevu_listesi')
    danisan = models.ForeignKey(Danisan, on_delete=models.CASCADE, related_name='gecmis_randevular')
    tarih = models.DateField()
    saat = models.TimeField()
    durum = models.CharField(max_length=20, choices=DURUM_CHOICES, default='beklemede')
    alinan_ucret = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    odeme_alindi = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tarih} - {self.uzman.ad_soyad} ({self.get_durum_display()})"

# 4. Mesajlaşma (Chat)
class Mesaj(models.Model):
    oda = models.CharField(max_length=255)
    gonderen = models.CharField(max_length=255)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    # HATA BURADAN KAYNAKLANIYORDU, BU SATIRI EKLE:
    okundu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.gonderen} - {self.oda}"

# 5. Müsaitlik (Çalışma Saatleri)
class Musaitlik(models.Model):
    uzman = models.ForeignKey(Uzman, on_delete=models.CASCADE, related_name='saatleri')
    gun = models.DateField()
    saat = models.TimeField()
    dolu_mu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.uzman.ad_soyad} - {self.gun} {self.saat}"

class Yorum(models.Model):
    uzman = models.ForeignKey(Uzman, on_delete=models.CASCADE, related_name='yorumlar')
    danisan = models.ForeignKey(Danisan, on_delete=models.CASCADE)
    puan = models.IntegerField(default=5) # 1-5 arası yıldız
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.danisan.user.first_name} -> {self.uzman.ad_soyad}"