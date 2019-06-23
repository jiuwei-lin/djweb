from django.urls import include, path
from .views import index, contact, post2db

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('post2db/', post2db),
]
