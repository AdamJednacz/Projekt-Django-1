from django.shortcuts import render, redirect
from .models import User,Comment,Like,Unlike
from .forms import UserForm,CommentForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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

def like(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    user = request.user  # Pobierz aktualnego użytkownika, który polubił komentarz (jeśli jest zalogowany)
    like, created = Like.objects.get_or_create(comment=comment, user=user)
    if created:
        # Zwiększ liczbę polubień dla komentarza
        comment.likes_count += 1
        comment.save()
        return redirect('home')
    else:
        return redirect('home')

def unlike(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    user = request.user  # Pobierz aktualnego użytkownika, który nie polubił komentarza (jeśli jest zalogowany)
    unlike, created = Unlike.objects.get_or_create(comment=comment, user=user)
    if created:
        # Zwiększ liczbę niepolubień dla komentarza
        comment.unlikes_count += 1
        comment.save()
        return redirect('home')
    else:
        return redirect('home')