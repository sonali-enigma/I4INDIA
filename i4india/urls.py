"""i4india URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login/',views.loginDetails),
    path('signup/',views.signupUser),
    path('logout/',views.logout),
    path('profile/',views.profile),
    path('contact/',views.contact),
    path('comingsoon/',views.comingsoon),
    path('aboutus/',views.aboutus),
    path('shop/<str:cat>/',views.shopDetails),
    path('services/',views.services),
    path('career/', views.career),
    path('product/<str:scat>/<int:num>/', views.productDetails),
    path('404/',views.error404),
    path('wishlist/<str:scat>/<int:num>/',views.wishlistDetails),
    path('wishlist/',views.wishlist),
    path('deletewishlist/<int:num>/',views.wishlistDelete),
    path('cart/', views.cartDetails),
    path('deletecart/<int:num>/',views.deletecart),
    path('password_reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
