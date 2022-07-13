
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index') # Como ta vazio vai ser a primeira pagina
]