from django.urls import path
from laboratorios import views


urlpatterns = [
    path('', views.home, name='laboratorio_home'),
    path('list/', views.laboratorio_list, name='laboratorio_list'),
    path('add/', views.LaboratorioCreateView.as_view(), name='laboratorio_add'),
    path('<slug:laboratorio_slug>/', views.laboratorio_detail, name='laboratorio_detail'),

    path('departamentos/<int:pk>/', views.DepartamentoDetailView.as_view(), name='depart_detail'),
]

urlpatterns = [
    path('', LaboratorioListView.as_view(), name='list'),
    path('create/', LaboratorioCreateView.as_view(), name='create'),
    path('<int:pk>/update/', LaboratorioUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', LaboratorioDeleteView.as_view(), name='delete'),
]
