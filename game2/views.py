from django.shortcuts import render

# Create your views here.
def tiktak(request):
    return render(request,'tiktak.html')
def index(request):
    return render(request,'index.html')
def stone(request):
    return render(request,'stone.html')
def animal(request):
    return render(request,'catchme.html')