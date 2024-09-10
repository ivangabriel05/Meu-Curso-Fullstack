from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URLs para a página inicial e informações gerais
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),

    # URLs para Usuários
    path('usuarios/', views.user_list, name='user_list'),
    path('usuarios/criar/', views.user_create, name='user_create'),
    path('usuarios/editar/<int:user_id>/', views.user_edit, name='user_edit'),
    path('usuarios/excluir/<int:user_id>/', views.user_delete, name='user_delete'),

    # URLs para Cursos
    path('cursos/', views.course_list, name='course_list'),
    path('cursos/criar/', views.course_create, name='course_create'),
    path('cursos/editar/<int:course_id>/', views.course_edit, name='course_edit'),
    path('cursos/excluir/<int:course_id>/', views.course_delete, name='course_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)