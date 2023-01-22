from email import header
from multiprocessing import context
from re import template
from unicodedata import category
from django.shortcuts import render
from my_api.models import Category, Book

def index(request):
    header_str = 'Hello, Python variable'
    context = {'var1' : header_str,
               'cal_num': len(Category.objects.all()),
               'book_num' : len(Book.objects.all())}
    return render(request, 'index.html', context)