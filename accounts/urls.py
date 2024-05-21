from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.home_index,name='homepage'),
    path('login/',views.login_user,name='user_login'),
    path('register-user/',views.register,name='user_register'),
    path('activate/<email_token>/',views.activate_email,name='activate'),
    path('logout/',views.logout_user,name='logoutuser')
  
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()