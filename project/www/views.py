from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = UserForm()

    users = User.objects.all()  # Pobierz wszystkich użytkowników

    return render(request, 'www/index.html', {'form': form, 'users': users})
