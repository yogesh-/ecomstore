from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50,unique=True,help_text='unique value for product page URL,created from name.')
	description = models.TextField()
	is_active = models.BooleanField(defaut=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return ('catalog_category', (), { 'category_slug': self.slug })


class Product(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(max_length=255, unique=True,
	help_text='Unique value for product page URL, created from name.')
	brand = models.CharField(max_length=50)
	sku = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=9,decimal_places=2)
	old_price = models.DecimalField(max_digits=9,decimal_places=2,
	blank=True,default=0.00)
	image = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	is_bestseller = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)
	quantity = models.IntegerField()
	description = models.TextField()
	meta_keywords = models.CharField(max_length=255,
	help_text='Comma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField(max_length=255,
	help_text='Content for description meta tag')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField(Category)

	def __unicode__(self):
		return self.name
	
	@models.permalink
	def get_absolute_url(self):
		return ('catalog_product', (), { 'product_slug': self.slug })
	def sale_price(self):
		if self.old_price > self.price:
		return self.price
		else:
		return None