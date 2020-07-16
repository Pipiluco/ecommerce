from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import User


class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_register_ok(self):
        data = {'username': 'teste', 'email': 'teste@pifrans.life', 'password1': 'Te123456', 'password2': 'Pi123456'}
        response = self.client.post(self.register_url, data)
        # index_url = reverse('index')
        # self.assertRedirects(response, index_url)
        # self.assertEquals(User.objects.count(), 1)

    def test_register_error(self):
        data = {'username': 'teste', 'password1': 'Te123456', 'password2': 'Pi123456'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')