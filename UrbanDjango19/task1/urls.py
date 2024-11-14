from django.urls import path
from . import views
from .views import platform, games, cart

urlpatterns = [
    path('', views.sign_up_by_django, name='sign_up_by_django'),
    path('django_sign_up/', views.sign_up_by_html, name='sign_up_by_html'),
    path('platform/', platform, name='platform'),
    path('games/', games, name='games'),
    path('cart/', cart, name='cart'),
]

