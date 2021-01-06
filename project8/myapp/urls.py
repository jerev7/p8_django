from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^$', views.listing, name="listing"),
	url(r'^(?P<product_id>[0-9]+)/$', views.results, name="results"),
	url(r'^search/$', views.search, name="search"),
	url(r'^product_detail/(?P<product_id>[0-9]+)/$', views.product_detail, name="product_detail"),
	url(r'^register/$', views.register, name="register")

]