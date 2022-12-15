from django.urls import path
from laboratorios import views


#urlpatterns = [
#    path('', views.home, name='laboratorio_home'),
#    path('list/', views.laboratorio_list, name='laboratorio_list'),
#    path('add/', views.LaboratorioCreateView.as_view(), name='laboratorio_add'),
#    path('<slug:laboratorio_slug>/', views.laboratorio_detail, name='laboratorio_detail'),

#    path('departamentos/<int:pk>/', views.DepartamentoDetailView.as_view(), name='depart_detail'),
#]

urlpatterns = [
    path('', views.LaboratorioListView.as_view(), name='list'),
    path('create/', views.LaboratorioCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.LaboratorioUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.LaboratorioDeleteView.as_view(), name='delete'),
]
