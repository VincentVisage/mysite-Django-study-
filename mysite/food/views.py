from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
from django.template import loader
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse('<h1>This is new item view</h1>')

def detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item':item,
    }
    return render(request, 'food/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form})

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form':form, 'item':item})

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'yes':
            item.delete()
            return redirect('food:index')
        elif confirm == 'no':
            return redirect('food:detail', id=id)
        
        return redirect('food:index')
    
    return render(request, 'food/delete-item.html', {'item':item})