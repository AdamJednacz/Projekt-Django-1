from .forms import BrandForm , ModelForm , UserForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
   
   
    return render(request, 'www/index.html', {})
    

def Brand_List(request):
    return render(request, 'www/brnad.html', {
        'brand': brand
        })

def Model_List(request):
    return render(request, 'www/model.html', {
        'model': model
        })

def User_List(request):
    return render(request, 'www/user.html', {
        'user': user
        })

def add_Brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = BrandForm()

    return render(request, 'www/add-brand.html', {'form': form})


def add_Model(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = ModelForm()

    return render(request, 'www/add-model.html', {'form': form})


def add_User(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = UserForm()

    return render(request, 'www/add-user.html', {'form': form})


def zapisano(request):
    return render(request, 'www/zapisano.html')