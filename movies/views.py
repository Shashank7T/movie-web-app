from django.shortcuts import render
from movies.models import Movies

# Create your views here.
def home_page(request):
    return render(request, 'movies/home_page.html')