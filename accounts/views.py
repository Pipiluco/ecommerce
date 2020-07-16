from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import UserAdminCreationForm

# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')




index = IndexView.as_view()
register = RegisterView.as_view()