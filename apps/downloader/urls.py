from django.urls import path

from .views import *


urlpatterns = [
    path('download/', download_video, name='download_video'),
    path('', home, name='home'),
]
