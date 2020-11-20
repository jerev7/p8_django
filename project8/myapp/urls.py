from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.listing),
	url(r'^(?P<category_id>[0-4]+)/$', views.detail),
]