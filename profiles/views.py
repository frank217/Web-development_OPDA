from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request,template,context)

def shop(request):
    context = {}
    template = 'shop.html'
    return render(request,template,context)

def about(request):
    context = {}
    template = 'about.html'
    return render(request,template,context)

def item_1(request):
    context = {}
    template = 'item_1.html'
    return render(request,template,context)