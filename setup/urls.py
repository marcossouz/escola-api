from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno
from escola.views import ListaAlunosMatriculados

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='alunos')
router.register('cursos', CursosViewSet, basename='cursos')
router.register('matriculas', MatriculasViewSet, basename='matriculas')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]
