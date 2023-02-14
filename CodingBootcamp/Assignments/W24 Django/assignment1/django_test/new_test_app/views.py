from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a lost of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, id):
    return HttpResponse(f'placeholder to display blog number: {id}')

def edit(request, id):
    return HttpResponse(f'placeholder to edit blog number: {id}')

def destroy(request, id):
    return redirect('blogs')

def jsonrsps(request):
    return JsonResponse({"is it working?": "yes", "really?!": "I think so"})


# def one_method(request):                # no values passed via URL
#     pass                                
    
# def another_method(request, my_val):	# my_val would be a number from the URL
#     return HttpResponse(f"this is the the number of bears {my_val}") # given the example above, my_val would be 23
    
# def yet_another(request, name):	        # name would be a string from the URL
#     pass                                # given the example above, name would be 'pooh'
    
# def one_more(request, id, color): 	# id would be a number, and color a string from the URL
#     pass                                # given the example above, id would be 17 and color would be 'brown'

# def root_method(request):
#     return HttpResponse("String response from root_method")
# def another_method(request):
#     return redirect("/redirected_route")
# def redirected_method(request):
#     return JsonResponse({"response": "JSON response from redirected_method", "status": True})