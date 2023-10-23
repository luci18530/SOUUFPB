from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('cursos/', views.cursos, name='cursos'),
    path('questionario/', views.questionario, name='questionario'),
    path('cursos/<int:curso_id>/', views.detalhes_curso, name='detalhes_curso'),
]