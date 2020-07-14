from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from catalog.models import Category, Product


class CatecoryTestCase(TestCase):
    def setUp(self):
        self.categoty = mommy.make('catalog.Category')

    def test_get_absolute_url(self):
        self.assertEquals(self.categoty.get_absolute_url(), reverse('catalog:category', kwargs={'slug': self.categoty.slug}))




class ProductTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make(Product, slug='product')

    def test_get_absolute_url(self):
        self.assertEquals(self.product.get_absolute_url(), reverse('catalog:product', kwargs={'slug': 'product'}))


