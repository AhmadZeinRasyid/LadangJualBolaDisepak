from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Products
from main.forms import ProductsForm

def show_main(request):
    context = {
        'npm' : '2406408395',
        'name' : 'Ahmad Zein Rasyid Siregar',
        'class' : 'PBP E'
    }

    return render(request, "main.html", context)

def add_product(request):
    form:ProductsForm = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main.html')

    context = {'form': form}
    return render(request, "add_product.html", context)

def see_details(request, id):
    products = get_object_or_404(Products, pk=id)
    context = {
        'products' : products
    }

    return render(request, "product_details.html", context)

def show_xml(request):
    product_list = Products.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Products.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, products_id):
    try:
        products_item = Products.objects.filter(pk=products_id)
        xml_data = serializers.serialize("xml", products_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Products.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, products_id):
    try:
        products_item = Products.objects.filter(pk=products_id)
        json_data = serializers.serialize("json", [products_item])
        return HttpResponse(json_data, content_type="application/json")
    except Products.DoesNotExist:
        return HttpResponse(status=404)
    