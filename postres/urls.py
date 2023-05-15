from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('recetas/', views.recetas, name="recetas"),
    path('saludables/', views.saludables, name="saludables"),
    path('nogluten/', views.sin_gluten, name="sgluten"),
    path('top10/', views.top_10, name="top10"),
    path('contacto/', views.contacto, name="contacto"),
]
