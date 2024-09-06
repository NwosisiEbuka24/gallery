from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import UpdateForm
from django.db.models import Q

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def homepage(request):
    product = Product.objects.all()
    return render(request, 'gallery/home.html', {'product':product})


@login_required(login_url='login')
def ViewPage(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'gallery/view.html', {'product':product})


@login_required(login_url='login')
def UpdateView(request, id):
    product = get_object_or_404(Product, id=id)
    form =  UpdateForm()
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user 
            form.save()
            return redirect('home')
    else:
        form = UpdateForm(instance=product)
    return render(request, 'gallery/edit.html', {'form':form, 'product':product})


def SearchQuery(request):
    query = request.GET.get('q')
    if query:
        product = Product.objects.filter(Q(name__icontains=query))
    else:
        product = Product.objects.none()
    return render(request, 'gallery/search.html', {'product': product})