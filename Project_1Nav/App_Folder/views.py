from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request,'App_Folder/index.html')

def relative_view(request):
    return render(request,'App_Folder/relative_url.html')

def other_view(request):
    return render(request,'App_Folder/other.html')
