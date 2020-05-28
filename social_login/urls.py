from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from social_login import views


urlpatterns = [
    path('admin/', admin.site.urls),         path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.home, name="home"),
]