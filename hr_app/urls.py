from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='hr_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profil/', views.profil, name='profil'),
    path('employes/', views.employe_list, name='employe_list'),
    path('employe/<int:pk>/', views.employe_detail, name='employe_detail'),
    path('employe/nouveau/', views.employe_create, name='employe_create'),
    path('employe/<int:pk>/modifier/', views.employe_update, name='employe_update'),
    path('employe/<int:pk>/archiver/', views.employe_archive, name='employe_archive'),
    path('stats/masse-salariale/', views.masse_salariale, name='masse_salariale'),
    path('mon-tableau-de-bord/', views.employe_dashboard, name='employe_dashboard'),
]
