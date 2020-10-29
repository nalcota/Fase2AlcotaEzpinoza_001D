from django.urls import path 
from copa import views

urlpatterns=[
	path('',views.index,name='index'),
	path('usuario/', views.UsuarioListView.as_view(), name='usuario'),
]