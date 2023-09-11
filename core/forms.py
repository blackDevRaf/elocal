from dataclasses import field, fields
from pyexpat import model
from .models import Product
from django import forms
class ProductForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["pictures"]=forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple":True}))

    class Meta:
        model=Product
        fields="__all__"
