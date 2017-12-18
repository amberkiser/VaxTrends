from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^coverage', views.coverage, name='coverage'),
    url(r'^$', views.index, name='index'),
]
