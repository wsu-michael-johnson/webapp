from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),
   path('actionurl', views.action),
   path('ffotf', views.index), ]
