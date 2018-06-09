from django.shortcuts import render, redirect
from movies.models import Movies


# Create your views here.
def home_page(request):
    user_query = str(request.GET.get('query', ''))
    result_set = Movies.objects.filter(Name__icontains=user_query)
    context = {'result_set': result_set}
    return render(request, 'movies/home_page.html', context)


# Create a new movie
def create(request):
    if request.method == 'POST':
        mov_obj = Movies(Name=request.POST.get('name'), Picture=request.POST.get('url'),
                         Rating=request.POST.get('rating'), Notes=request.POST.get('notes'))
        mov_obj.save()
    return redirect('/')
