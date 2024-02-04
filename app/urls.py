from django.urls import path
from .views import core, detail, about, galerea, galerea_detail

urlpatterns = [
    path('', core, name='core'),
    path("detail/<int:id>", detail, name="detail"),
    path('about', about, name='about'),
    path('galerea', galerea, name='galerea'),
    path('galerea/<int:id>', galerea_detail, name='gal_d'),
]