from django.urls import include, path
from .views import index

urlpatterns = [
    path('', index),
    path('<int:tvno>/', index, name='tv-url')
]
