from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        url, created = URL.objects.get_or_create(original_url=original_url)
        return render(request, 'app/home.html', {'short_url': url.short_url})
    return render(request, 'app/home.html')

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)
