from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^$', views.listing, name="listing"),
	url(r'^(?P<product_id>[0-6]+)/$', views.detail, name="detail"),
	url(r'^search/$', views.search, name="search")
]