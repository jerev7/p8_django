from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^$', views.listing, name="listing"),
	url(r'^(?P<category_id>[0-4]+)/$', views.detail, name="detail"),
	url(r'^search/$', views.search, name="search")
]