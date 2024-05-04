from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to="images")
    create = models.DateTimeField(auto_now=False,auto_now_add=True)


    def __str__(self) :
        return self.name




class Model(models.Model):
    name = models.CharField(max_length=40)
    brand = models.ManyToManyField(Brand)
    create = models.DateTimeField(auto_now=False,auto_now_add=True)
    
    def __str__(self) :
        return self.name





class User(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    userphoto = models.ImageField(upload_to='images')
    email = models.EmailField(max_length=100)
    # brand = models.ManyToManyField(Model)
    photo = models.ImageField(upload_to='images')
    text = models.CharField(max_length=200,default='')
    create = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.surname 