from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Item, Purchase

def index(request):
    return HttpResponse(
        '''
            <!doctype html>
            <h1>A new project 'Shop' has been created successfully.</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=file>
              <input type=submit value=Upload>
            </form>
            '''

    )

def list_item(request):
    item = Item.objects.all().order_by('-name')[:5]
    context = {
        'items': item
    }
    return render(request, 'list_item.html', context)
def detail_item(request, item_id):
    purchase = get_object_or_404(Purchase, id=item_id)
    purchase_list = Purchase.objects.filter(item_id=item_id)
    return render(request, 'detail_item.html', {'purchase': purchase, 'purchase_list': purchase_list})


