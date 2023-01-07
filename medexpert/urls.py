from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'medexpert'
urlpatterns = [
                  path('', auth_views.LoginView.as_view(template_name='medexpert/login.html'), name='login'),
                  path('register/', views.Register, name='register'),
                  path('home', views.home, name='home'),
                  path('update/', views.updateview, name='updateview'),
                  path('hospitals', views.view_hospital, name='view_hospital'),
                  path('firstaid', views.view_firstaid, name='view_firstaid'),
                  path('emergency', views.submit, name='submit'),
                  path('maps', views.view_maps, name='view_maps'),
                  path('message', views.send, name='send'),

                  path('register/', views.Register, name='register'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
