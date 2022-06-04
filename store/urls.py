from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.home, name='home'),

    path("admin/login/", views.AdminLoginView.as_view(), name="adminlogin"),
    path("admin/logout/", views.AdminLogoutView.as_view(), name="adminlogout"),
    path("admin/", views.AdminHomeView.as_view(), name="adminhome"),
]
