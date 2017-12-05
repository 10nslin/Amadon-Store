# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
prices={
    '1015':19.99,
    '1016':29.99,
    '1017':4.99,
    '1018':49.99
}
def index(request):
    return render(request,'amadon/index.html',{'prices':prices})

def process(request):
    try:
        request.session['count']
    except KeyError:
        request.session['count']=0
        request.session['total']=0

    request.session['count']+=int(request.POST['quantity'])
    quantity=int(request.POST['quantity'])
    product_id=request.POST['product_id']
    request.session['order']=quantity*int(prices[product_id])
    request.session['total']=request.session['total']+request.session['order']

    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')

def clear(request):
    del request.session['count']
    del request.session['order']
    del request.session['total']
    return redirect('/')