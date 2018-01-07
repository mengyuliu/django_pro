from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.homepage, name='index'),
        url(r'^post/(?P<slug>\w+)$', views.showpost, name='post'),
        # url(r'^post/(\w+)$', views.showpost, name='post'),
]