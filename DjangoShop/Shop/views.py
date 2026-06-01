from django.shortcuts import render
from django.urls import reverse

def shop(request):
    home = reverse('home')
    data = {
        'home': home,
    }
    return render(request, 'shop.html', data)
