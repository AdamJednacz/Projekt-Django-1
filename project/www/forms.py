from django import forms

from .models import Brand , Model , User

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'