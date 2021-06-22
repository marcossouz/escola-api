from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from escola.views import AlunosViewSet, CursosViewSet

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='alunos')
router.register('cursos', CursosViewSet, basename='cursos')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
