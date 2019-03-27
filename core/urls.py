"""cld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core import views
from django.urls import path


urlpatterns = [
     path('livros/', views.LivroListServiceView.as_view(), name='livros'),
     path('cadastrarLivro/', views.CadastrarLivroServiceView.as_view(), name='cadastrarLivro'),
     path('atualizarLivro/', views.AtualizarLivroServiceView.as_view(), name='atualizarLivro'),
     path('excluirLivro/', views.ExcluirLivroServiceView.as_view(), name='excluirLivro'),
]
