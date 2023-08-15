from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.urls import reverse
from .forms import *
from .models import product, order
from .cart import Cart

def index(request):
	revs = []
	cart_products = []
	coffee = []
	syrop = []
	suvenir = []
	total_price = 0.00

	form_review = add_review()
	reviews = review.objects.all()
	products = product.objects.all()
	cart = request.session.get('cart')


	for product_id in cart:
		cart_products.append(cart[product_id])
	for item in products:
		if (item.category == 'CG'):
			coffee.append(item)
		elif (item.category == 'SP'):
			syrop.append(item)
		elif (item.category == 'SR'):
			suvenir.append(item)


	for item in cart_products:
		total_price += float(item['price'])
	if len(reviews) >= 4:
		for i in range(4):
			revs.append(reviews[i])
	else:
		revs = reviews


	context = {
		'total_price' : total_price,
		'cart_products' : cart_products,
		'form_review' : form_review,
		'four_rev' : revs,
		'suvenir' : suvenir,
		'coffee' : coffee,
		'syrop' : syrop,
		}
	return render(request, 'index.html', context)



def create_review(request):
	if request.method == 'POST':
		form = add_review(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('main:index'))
	return HttpResponseRedirect(reverse('main:index'))


@require_POST
def cart_add(request):
	product_id = request.POST['product_id']
	cart = Cart(request)
	prod = get_object_or_404(product, id=product_id)
	cart.add(product=prod,
		update_quantity=True)
	return HttpResponseRedirect(reverse('main:index'))

def cart_remove(request):
	cart = Cart(request)
	product_id = request.POST['product_id']
	prod = get_object_or_404(product, id=product_id)
	cart.remove(prod)
	return HttpResponseRedirect(reverse('main:index'))

def cart_minus(request):
	cart = Cart(request)
	product_id = request.POST['product_id']
	prod = get_object_or_404(product, id=product_id)
	cart.minus(prod)
	return HttpResponseRedirect(reverse('main:index'))

def create_order(request):
	cart = request.session.get('cart')
	cart_products = []
	cart_price = request.POST['total_price']
	adres = request.POST['adres']

	if cart:
		for product_id in cart:
			cart_products.append(cart[product_id]['name'])
		cart_products = '|'.join(cart_products)
	order_add = order(username_client = 'user', list_product = cart_products, total_price = cart_price, adres = adres)
	order_add.save()
	return HttpResponseRedirect(reverse('main:index'))




