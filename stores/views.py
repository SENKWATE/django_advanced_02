from django.shortcuts import render, redirect
from .models import Store, generate_slug
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)


def store_detail(request,slug):
    store = Store.objects.get(slug=slug)
    
    context = {
        "store": store, # pass slug 
    }
    return render(request, 'store_detail.html', context)

def store_create(request):
    form = StoreModelForm()
    if request.method == "POST":
        form = StoreModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'store_create.html', context)
