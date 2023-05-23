from django.shortcuts import render
from .forms import *

def home(request):
    return  render(request, 'book/home.html')

def admin_view(request):
    return render(request, 'book/admin_page.html')

def add_book(request):
    form = AddBookForm()

    context = {'form': form, 'data': 'data'}
    return render(request, 'book/add_book.html', context)