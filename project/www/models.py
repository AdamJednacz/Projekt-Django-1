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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return f'Comment on {self.created_at}'
    


class Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    def __str__(self):
        return f'Like on {self.comment}'

class Unlike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    def __str__(self):
        return f'Unlike on {self.comment}'