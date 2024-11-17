from django.urls import path
from . import views
from .views import platform, games, cart, post_list

urlpatterns = [
    path('', post_list, name='home'),  # Здесь мы добавляем маршрут с именем 'home'
    path('django_sign_up1/', views.sign_up_by_django, name='sign_up_by_django'),
    path('django_sign_up2/', views.sign_up_by_html, name='sign_up_by_html'),
    path('post_list/', post_list, name='post_list'),
    path('platform/', platform, name='platform'),
    path('games/', games, name='games'),
    path('cart/', cart, name='cart'),
]

