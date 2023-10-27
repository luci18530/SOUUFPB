from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('home', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('cursos/', views.cursos, name='cursos'),
    path('teste/', views.teste, name='teste'),
    path('perfil/', views.perfil, name='perfil'),
    path('get_data/', views.get_data, name='get_data'),
    path('cursos/<int:curso_id>/', views.detalhes_curso, name='detalhes_curso'),
]