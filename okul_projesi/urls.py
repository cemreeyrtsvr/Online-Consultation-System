from django.contrib import admin
from django.urls import path
from ana_sayfa import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.giris_sayfasi, name='giris_sayfasi'),
    path('home/', views.ana_sayfa, name='ana_sayfa'),

    path('login/<str:rol>/', views.login_sayfasi, name='login_sayfasi'),
    path('kayit/<str:rol>/', views.kayit_ol, name='kayit_ol'),

    path('profil/', views.profil_sayfasi, name='profil_sayfasi'),
    path('profil/duzenle/', views.profil_duzenle, name='profil_duzenle'),

    path('bolum/<str:bolum_adi>/', views.bolum_detay, name='bolum_detay'),
    path('logout/', views.logout, name='logout'),

    path('danisan-paneli/', views.danisan_sayfasi, name='danisan_sayfasi'),

    # --- ÖDEME VE RANDEVU KESİNLEŞTİRME ---
    path('odeme/<int:saat_id>/', views.odeme_yap, name='odeme_yap'),
    path('odeme-sayfasi/', views.odeme_sayfasi, name='odeme_sayfasi'),

    # --- CÜZDAN VE BAKİYE İŞLEMLERİ (YENİ) ---
    path('bakiye-yukle/', views.bakiye_yukle, name='bakiye_yukle'),
    path('cuzdan-ode/<int:saat_id>/', views.cuzdanla_ode, name='cuzdanla_ode'),

    # --- UZMAN SEANS VE RANDEVU YÖNETİMİ ---
    path('uzman/saat-ekle/', views.uzman_saat_ekle, name='uzman_saat_ekle'),
    path('randevu-sec/<int:uzman_id>/', views.randevu_saat_sec, name='randevu_saat_sec'),

    # --- UZMAN ONAY/RED AKSİYONLARI ---
    path('randevu-onayla/<int:randevu_id>/', views.randevu_onayla, name='randevu_onayla'),
    path('randevu-reddet/<int:randevu_id>/', views.randevu_reddet, name='randevu_reddet'),

    # --- CHAT / MESAJLAŞMA SİSTEMİ (YENİ EKLENEN) ---
    path('chat/<str:oda_adi>/', views.chat_odasi, name='chat_odasi'),
]

# Profil fotoğraflarının görünmesi için gerekli ayar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)