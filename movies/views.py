from django.shortcuts import render
from movies.models import Movies


# Create your views here.
def home_page(request):
    user_query = str(request.GET.get('query', ''))
    result_set = Movies.objects.filter(Name__icontains=user_query)
    context = {'result_set': result_set}
    return render(request, 'movies/home_page.html', context)
