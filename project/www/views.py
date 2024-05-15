from django.shortcuts import render, redirect
from .models import User,Comment,Like,Unlike
from .forms import UserForm,CommentForm
from django.db.models import F
def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UserForm()

    users = User.objects.all()  

    return render(request, 'www/index.html', {'form': form, 'users': users})


def comment(request):
    users = User.objects.all()  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_id = form.cleaned_data['user_id']
            user = User.objects.get(pk=user_id)
            comment = Comment.objects.create(text=text, user=user)
            return redirect('comments')
    else:
        form = CommentForm()  

    return render(request, 'www/comments.html', {'form': form, 'users': users})

def like(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
     
        if comment_id:
            comment = Comment.objects.get(id=comment_id)
    
            try:
                like = Like.objects.get(comment=comment)
                like.delete() 
                comment.like_set.update(clicks=F('clicks') - 1) 
            except Like.DoesNotExist:
                Like.objects.create(comment=comment)
                comment.like_set.update(clicks=F('clicks') + 1)  

            return redirect('comments')

def unlike(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
   
        if comment_id:
            comment = Comment.objects.get(id=comment_id)
     
            try:
                unlike = Unlike.objects.get(comment=comment)
                unlike.delete()  
                comment.unlike_set.update(clicks=F('clicks') - 1)  
            except Unlike.DoesNotExist:
                Unlike.objects.create(comment=comment)
                comment.unlike_set.update(clicks=F('clicks') + 1)  

            return redirect('comments')
    total_likes = Comment.objects.aggregate(sum('like__clicks'))
    total_unlikes = Comment.objects.aggregate(sum('unlike__clicks'))
    return render(request, 'www/comments.html', {'total_likes': total_likes, 'total_unlikes': total_unlikes})        


def about_us(request):
        return render(request, 'www/about_us.html', {})

def contact(request):
        return render(request, 'www/contact.html', {})
