from django.urls import path

from .views import EmpresaCreate, EmpresaEdit

urlpatterns = [ 
    path('create-empresa', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar-empresa/<int:pk>/', EmpresaEdit.as_view(), name='editar_empresa'),
]