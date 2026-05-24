from django.contrib import admin
from .models import Uzman, Danisan, Randevu, Musaitlik

@admin.register(Uzman)
class UzmanAdmin(admin.ModelAdmin):
    list_display = ('ad_soyad', 'unvan', 'brans', 'ucret', 'bakiye', 'aktif_mi')
    list_filter = ('brans', 'aktif_mi')
    search_fields = ('ad_soyad', 'unvan')

@admin.register(Danisan)
class DanisanAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefon', 'bakiye')
    search_fields = ('user__first_name', 'user__last_name')

@admin.register(Randevu)
class RandevuAdmin(admin.ModelAdmin):
    list_display = ('tarih', 'saat', 'uzman', 'danisan', 'durum', 'alinan_ucret')
    list_filter = ('durum', 'tarih')

@admin.register(Musaitlik)
class MusaitlikAdmin(admin.ModelAdmin):
    list_display = ('uzman', 'gun', 'saat', 'dolu_mu')
    list_filter = ('gun', 'dolu_mu')