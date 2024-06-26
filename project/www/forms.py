from django import forms

from .models import  User,Comment



class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    userphoto = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose your profile photo'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose your car photo'}))
    text = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'placeholder': 'Discription'}))
    class Meta:
        model = User
        fields = '__all__'


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder': 'Write your comment here...','class':'add_comment_text_area'}))
    user_id = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Comment
        fields = ['text']
