# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm, BookForm, AuthorForm
from .helper import handle_uploaded_file
from .models import Book, Author
from django.utils.translation import activate, ugettext as _
from django.template import Context, RequestContext

from django.contrib import messages
from django.core import serializers

import pdb
# Create your views here.
def index(request):
    form = UploadFileForm(request.POST, request.FILES)
    LANGUAGE_CODE = request.LANGUAGE_CODE
    activate(LANGUAGE_CODE)
    return render_to_response('book/index.html', locals())



def list_book(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'book/list_book.html', {'books': books})


# Imaginary function to handle an uploaded file.

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for i in request.FILES.iteritems():
                print i.count(), i.index()
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/book/')
    else:
        form = UploadFileForm()
    return render(request, 'book/upload.html', {'form': form})

def upload_book(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'book/upload_book.html', {'form':form})
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return HttpResponse("good")

def add_author(request):
    if request.method == 'GET':
        form = AuthorForm()
        return render(request, 'book/add_author.html', locals())
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid(): # will check name unique
            author_form.save()
            return HttpResponse('Author added')
        else:
            print author_form.errors.as_data()
            form = AuthorForm()
            messages.warning(request, 'Author exists')  
            return render(request, "book/add_author.html", locals())

def all_book(request):
    data = serializers.serialize("json", Book.objects.all(), fields=('name',))
    return HttpResponse(data)
