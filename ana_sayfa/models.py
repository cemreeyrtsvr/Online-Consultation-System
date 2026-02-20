from django.db import models

class Mesaj(models.Model):
    oda = models.CharField(max_length=50) # <-- YENİ: Mesaj kime ait? (Örn: dyt-ayse)
    gonderen = models.CharField(max_length=100)
    icerik = models.TextField(blank=True, null=True)
    dosya = models.FileField(upload_to='chat_dosyalari/', blank=True, null=True)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.oda}] {self.gonderen}"