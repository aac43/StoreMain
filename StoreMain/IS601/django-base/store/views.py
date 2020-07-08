from django.shortcuts import render
from django.http import HttpResponse
'''def index(request):
    return HttpResponse("Nothing to see here... yet.")
'''    
def product(request):
    return render(request, 'product.html')  
def index(request):
    return HttpResponse("Nothing to see here... yet.") 
'''
def product(request):
    return render(request, 'product.html')  
'''