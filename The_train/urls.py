from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('signup/', views.user_signup, name="signup"),
    path('logout/', views.user_logout, name="logout"),
    path('booking/', views.booking, name="booking"),
    path('comp/', views.comp, name="comp"),
    path('display/', views.display, name="display"),
]

urlpatterns += staticfiles_urlpatterns()