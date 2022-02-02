from django.shortcuts import render

def home_page(request):
    template = 'blog/home.html'
    return render(request, template)