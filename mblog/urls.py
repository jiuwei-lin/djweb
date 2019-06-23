from django.urls import include, path
from mblog.views import homepage, showpost

urlpatterns = [
    path('', homepage),
    path('post/<slug:slug>/', showpost),
]
