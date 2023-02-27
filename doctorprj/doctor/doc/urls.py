from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index),
    path('registration/', views.registration),
    path('login/', views.login),
    path('logindata/', views.logindata),
    path('table/',views.table),
    path('update/<int:tid>/',views.update),
    path('updatedata/',views.updatedata),
    path('delete/<int:tid>/',views.delete),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
