from django.urls import path
from .views import class_template, func_template


urlpatterns = [
    path('class_view/', class_template, name='class_view'),
    path('func_view/', func_template, name='func_view'),
]
