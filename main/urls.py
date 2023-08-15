from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('create_review', views.create_review, name = 'create_review'),
	path('add', views.cart_add, name='cart_add'),
	path('minus', views.cart_minus, name='cart_minus'),
	path('remove', views.cart_remove, name='cart_remove'),
	path('create_order', views.create_order, name='create_order'),
]