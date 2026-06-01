from django.shortcuts import render
from django.urls import reverse


def home(request):
    shop = reverse('shop')
    data = {
    'shop': shop,
    }
    return render(request, 'home.html', data)
# Create your views here.
