from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def create_user(request):
    print('Got the POST info..................')
    name_from_form = request.POST['name']
    name_from_email = request.POST['email']
    context = {
        'name_on_template' : name_from_form,
        'email_on_template' : name_from_email
    }
    return redirect('/success')

def success(request):
    return render(request, 'show.html')