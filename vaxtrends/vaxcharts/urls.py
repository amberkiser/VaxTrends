from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^coverage', views.coverage, name='coverage'),
    url(r'^schedule', views.schedule, name='schedule'),
    url(r'^vpd', views.vpd, name='vpd'),
    url(r'^datasources', views.datasources, name='datasources'),
    url(r'^$', views.index, name='index'),
]
