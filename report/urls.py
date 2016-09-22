from django.conf.urls import url
from report import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^report/$', views.report, name='report'),
]