from django.shortcuts import render, redirect
from .models import User,Comment,Like
from .forms import UserForm,CommentForm
def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UserForm()

    users = User.objects.all()  # Pobierz wszystkich użytkowników

    return render(request, 'www/index.html', {'form': form, 'users': users})




def comment(request):
    users = User.objects.all()  # Pobierz wszystkich użytkowników
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_id = form.cleaned_data['user_id']
            user = User.objects.get(pk=user_id)
            comment = Comment.objects.create(text=text, user=user)
            return redirect('comments')
    else:
        form = CommentForm()  # Utwórz nowy formularz, gdy strona zostanie załadowana

    return render(request, 'www/comments.html', {'form': form, 'users': users})


def like_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    Like.objects.create(comment=comment, like=True)
    return redirect('home')

def unlike_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    Like.objects.create(comment=comment, like=False)
    return redirect('home')



