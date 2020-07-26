from django.urls import path
from laboratorios import views


urlpatterns = [
    path('', views.home, name='laboratorio_home'),
    path('list/', views.laboratorio_list, name='laboratorio_list'),
    path('add/', views.LaboratorioCreateView.as_view(), name='laboratorio_add'),
    path('<slug:laboratorio_slug>/', views.laboratorio_detail, name='laboratorio_detail')
]
