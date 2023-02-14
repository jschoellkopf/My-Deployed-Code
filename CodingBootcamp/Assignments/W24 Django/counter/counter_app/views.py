from django.shortcuts import render, redirect

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    print(request.session['counter'])
    return render(request, 'index.html')

def destroy(request):
    if 'counter' in request.session:
        del request.session['counter']
    else:
        print("key 'counter' does NOT exist")
    return redirect('/')