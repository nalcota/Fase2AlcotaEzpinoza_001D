from django.urls import path 
from copa import views

urlpatterns=[
	path('',views.index,name='index'),
	path('usuario/', views.UsuarioListView.as_view(), name='usuario'),
<<<<<<< HEAD
	path('usuario/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
	path('form/', views.form, name='form'),
    path('galeria/', views.galeria, name='galeria'),
=======
>>>>>>> 22797853a16a9c39941318cb8f32cf64cb643fdb
]