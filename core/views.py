from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import ContactForm


# Create your views here.

User = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()




def contact(request):
    success = False
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.send_mail()
        success = True

    context = {'form': form, 'success': success}

    return render(request, 'contact.html', context)


