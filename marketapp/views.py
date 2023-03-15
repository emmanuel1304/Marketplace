from django.shortcuts import render, get_object_or_404
from .models import Item, Categories
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Categories.objects.all()
    context = {'items':items, 'categories':categories}
    return render(request, 'marketapp/index.html', context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk)
    context = {'item': item}
    return render(request, 'marketapp/item_detail.html', context)
