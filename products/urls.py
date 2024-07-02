from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
#   path('<slug>/',)
    path('<slug>',views.get_product,name='get_product'),
    path('add/<slug>',views.addtocart,name='addtocart'),
    path('buy/<slug>',views.buynow,name='buynow'),
    path('yourorders/',views.yourorders,name='yourorders'),
    path('cart/',views.yourcart,name='yourcart'),
    path('cart/delete/<uid>',views.deletecart,name='deletecart'),
    path('cart/savelater/<uid>',views.savelater,name='savelatercart'),
    path('savelater/',views.yoursavelater,name='yoursavelater'),
    path('cart/placeorder/',views.buyfromcart,name='buyfromcart')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()