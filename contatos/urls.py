from django.urls import path
from . import views # importa o views da pasta

# urls das paginas
urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>', views.vercontato, name='vercontato'),

]