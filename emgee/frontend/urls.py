from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^frontend', views.frontend, name='frontend'),
    url(r'^logs', views.logs, name='logs'),
]
