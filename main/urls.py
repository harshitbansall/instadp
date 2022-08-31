from django.urls import path

from .views import Home, ReturnImage

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('returnImage', ReturnImage.as_view(), name='ReturnImage'),

]
