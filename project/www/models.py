from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    userphoto = models.ImageField(upload_to='images')
    email = models.EmailField(max_length=100)
    photo = models.ImageField(upload_to='images')
    text = models.CharField(max_length=100, default='')
    create = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.surname 

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Klucz obcy do użytkownika
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def count_likes(self):
        return self.like_set.filter(like=True).count()

    def __str__(self):
        return f'Comment on {self.created_at}'
    
class Like(models.Model):
    LIKE_CHOICES = [
        (True, 'Like'),
        (False, 'Unlike')
    ]

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(choices=LIKE_CHOICES)


    def __str__(self):
        like_type = 'Like' if self.like else 'Unlike'
        return f'{self.user} {like_type} on {self.comment.created_at}'