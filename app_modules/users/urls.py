from django.urls import path
from app_modules.users import views

app_name = "users"

urlpatterns = [
    path('', views.DashboardView.as_view(), name="dashboard"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
]
