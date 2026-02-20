from django.contrib import admin
from django.urls import path
from ana_sayfa import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.giris_sayfasi, name='giris'),
    path('login/<str:rol>/', views.login_sayfasi, name='login'),
    path('ogrenci/', views.ana_sayfa, name='ana_sayfa'),
    path('danisan/', views.danisan_sayfasi, name='danisan_sayfasi'),
    path('bolum/<str:bolum_adi>/', views.bolum_detay, name='bolum_detay'),
    path('odeme/', views.odeme_sayfasi, name='odeme_sayfasi'),

    # --- YENİ: PROFİL SAYFASI YOLU ---
    path('profil/', views.profil_sayfasi, name='profil_sayfasi'),

    path('mesaj-gonder/', views.mesaj_gonder, name='mesaj_gonder'),
    path('mesajlari-getir/', views.mesajlari_getir, name='mesajlari_getir'),
]