from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.register_form, name='register_form'),
	url(r'^registered/', views.register_list, name='register_list'),
]
