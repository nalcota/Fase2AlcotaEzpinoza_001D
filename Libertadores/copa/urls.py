from django.urls import path 
from copa import views

urlpatterns=[
	path('',views.index,name='index'),
	path('usuario/', views.UsuarioListView.as_view(), name='usuario'),
	path('usuario/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
	path('form/', views.form, name='form'),
    path('galeria/', views.galeria, name='galeria'),
]

urlpatterns +=[
    path('usuario/create/', views.UsuarioCreate.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/update/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/delete/', views.UsuarioDelete.as_view(), name='usuario_delete'),

]