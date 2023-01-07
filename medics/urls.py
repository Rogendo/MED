from django.urls import path
from medics import views
from django.conf import settings
from medics import views as user_views

from django.conf.urls.static import static

app_name='medics'
urlpatterns = [
      path('',views.home, name='home'),
      path('emergency',views.viewemergency,name= 'viewemergency'),
      path('message', views.viewmessage, name='viewmessage'),


]
