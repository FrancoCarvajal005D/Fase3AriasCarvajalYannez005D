from django.urls import path 
from noticia import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contacto/',views.contacto, name='contacto'),
    path('quienes_somos/',views.quienes_somos, name='quienes_somos'),
    path('categorias/',views.categorias, name='categorias'),
    path('peticion/',views.peticion, name='peticion'),
]

urlpatterns+=[
    path('contacto/create/', views.ContactoCreate.as_view(), name='contacto_create'),
    path('contacto/<int:pk>/update/', views.ContactoUpdate.as_view(), name='contacto_update'),
    path('contacto/<int:pk>/delete/', views.ContactoDelete.as_view(), name='contacto_delete'),
    path('peticion/<int:pk>/update/', views.peticionUpdate.as_view(), name='peticion_update'),
    path('peticion/<int:pk>/delete/', views.peticionDelete.as_view(), name='peticion_delete'),
]