from django.db import models
from django.utils.timezone import now

class review(models.Model):
	username_client = models.CharField(max_length = 100, blank=False)
	review = models.TextField(max_length = 255, blank = False)
	date = models.DateTimeField(default=now())
	def __str__(self):
		return self.username_client


class order(models.Model):
	username_client = models.CharField(max_length=100, blank=False)
	list_product = models.TextField(blank=False)
	total_price = models.DecimalField(max_digits=20, decimal_places=2)
	adres = models.CharField(max_length=100, blank=False)
	date = models.DateTimeField(default=now())
	def __str__(self):
		return self.list_product

CATEGORY = [
	('CG', 'Кофе в зернах'),
	('SP', 'Сироп'),
	('SR', 'Сувенир'),
]

class product(models.Model):
	name = models.CharField(max_length=100, blank=False)
	description = models.TextField(max_length=255, blank=False)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.CharField(max_length=2, blank = False, choices=CATEGORY)
	def __str__(self):
		return self.name

