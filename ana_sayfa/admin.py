from django.contrib import admin
from .models import Mesaj

@admin.register(Mesaj)
class MesajAdmin(admin.ModelAdmin):
    list_display = ('gonderen', 'icerik', 'tarih')
    list_filter = ('gonderen', 'tarih')
    search_fields = ('icerik', 'gonderen')