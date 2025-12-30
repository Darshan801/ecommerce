from django.urls import path , include
from authcart import views

urlpatterns = [
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),
         name='activate')
]
