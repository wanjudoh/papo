from django import forms
from .models import Market 

class PostForm(forms.ModelForm): 
    class Meta:
        model = Market
        fields = ['title','summary', 'body','image', 'pptfile']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False