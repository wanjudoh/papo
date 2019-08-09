from django import forms 
from .models import Suggest

class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggest # form 에서 사용할 모델이 Suggest임을 명시
        fields = ['title','content']

    