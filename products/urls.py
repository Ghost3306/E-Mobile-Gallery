from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
#   path('<slug>/',)
    path('<slug>',views.get_product,name='get_product'),
    path('add/<slug>',views.addtocart,name='addtocart')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()