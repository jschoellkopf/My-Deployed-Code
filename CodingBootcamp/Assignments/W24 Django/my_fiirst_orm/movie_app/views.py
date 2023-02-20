from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    context = {
        'all_movies' : Movie.objects.all()
    }
    return render(request, 'app_one/index.html', context)