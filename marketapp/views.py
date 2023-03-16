from django.shortcuts import render, get_object_or_404
from .models import Item, Categories
from .forms import SignUpForm, NewItemForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Categories.objects.all()
    context = {'items':items, 'categories':categories}
    return render(request, 'marketapp/index.html', context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk)
    related_item = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {'item': item, 'related_item': related_item}
    return render(request, 'marketapp/item_detail.html', context)

def new(request):
    form  = NewItemForm
    context = {'form': form}
    return render(request, 'marketapp/new_item_form.html', context) 