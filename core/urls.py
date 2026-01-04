from django.urls import path
from core import views


app_name = "core"

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('signin/',views.sign_in,name='sign_in'),
    path('checkout/',views.checkout,name='checkout'),

]

