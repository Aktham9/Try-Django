from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ProductForm, RawProductForm
# Create your views here.


# def product_create_view(request):
#     form= RawProductForm()
#     if request.method == "POST":
#         form= RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)// here clean_data return a dictionary
#             Product.objects.create(**form.cleaned_data)// here to save data in the DB or in the model
#             form = RawProductForm()
#     context={"form":form}
#     return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#     if request.method == 'POST':
#         #print("request.get is:  ", request.GET)
#         #print("request.post is: ", request.POST)
#         my_new_title= request.POST.get('title')
#         print(my_new_title)
#     context = {}
#     return render(request, 'products/product_create.html', context)
#
#

#








# for initiating data in the form
# def render_initial_data(request):
# ## we initiate dict to initiate the title in the form
#     initial_data={
#         "title": "my this awsome title"
#     }
# ## creating the object to edit the object which has id=1 in the DB
#     obj= Product.objects.get(id=1)
#     form = ProductForm(request.POST or None,initial=initial_data) ## we must add ,  instance=obj if we need to edit object in DB
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#
#     context = {"form": form}
#     return render (request, 'products/product_create.html', context)


# def Dynamic_url(request, id):
#     #obj= Product.objects.get(id=id)
#     #obj=get_object_or_404(Product, id=id)
#     try:
#         obj= Product.objects.get(id= id)
#     except Product.DoesNotExist:
#         raise Http404
#
#
#     context={"object": obj}
#
#
#     return  render(request, 'products/for_render.html', context)


############################################################

def product_list_view(request):
    queryset= Product.objects.all()

    context = {"object": queryset}
    return render(request, 'products/product_list.html', context)

def product_detail_view(request, id):
    obj= get_object_or_404(Product, id=id)
    #context={
       ## "title":obj.title,
        #"price":obj.price,
       # "description":obj.description,

   # }
    context= {
        'object': obj
    }
    return render (request, 'products/product_detail.html', context)

def product_create_view(request):
    #if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductForm()


        context = {'form': form}
        return render(request, 'products/product_create.html', context)

def product_update_view(request, id):
## we initiate dict to initiate the title in the form
    # initial_data={
    #     "title": "my this awsome title"
    # }
## creating the object to edit the object which has id=1 in the DB
    obj= get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj) ## we must add ,  instance=obj if we need to edit object in DB
    if form.is_valid():
        form.save()
        form = ProductForm()


    context = {"form": form}
    return render (request, 'products/product_create.html', context)


def product_delete_view(request, id):
    obj= get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')

    context = {"object": obj}

    return render(request, 'products/product_delete.html', context)
