from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def test(request):
    return HttpResponse('This is a test page')

def login(request):
    return render(request, 'registration/login.html')