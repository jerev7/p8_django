from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^$', views.listing, name="listing"),
	url(r'^(?P<product_id>[0-9]+)/$', views.results, name="results"),
	url(r'^search/$', views.search, name="search"),
	url(r'^product_detail/(?P<product_id>[0-9]+)/$', views.product_detail, name="product_detail"),
	url(r'^register/$', views.register, name="register"),
	url(r'^registration_ok/$', views.registration_ok, name="registration_ok"),
	url(r'^logged_out/$', views.logged_out, name="logged_out"),
	url(r'^user_products/$', views.user_products, name="user_products"),
	url(r'^save_product/(?P<product_selected_id>[0-9]+)/(?P<substitution_id>[0-9]+)/$', views.save_product, name="save_product")
]