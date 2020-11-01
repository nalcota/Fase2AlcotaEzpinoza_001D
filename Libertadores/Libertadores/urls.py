from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
<<<<<<< HEAD
  #  path('admin/', admin.site.urls),
=======
    path('admin/', admin.site.urls),
>>>>>>> 22797853a16a9c39941318cb8f32cf64cb643fdb
    path('copa/',include('copa.urls'))
   

]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

