from django import forms
from .models import Product

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px;'}),
            'image': forms.FileInput(attrs={'style': 'padding: 10px;'}),

            'description': forms.Textarea(attrs={'style': 'width: 100%; padding: 10px;'}),
        }
