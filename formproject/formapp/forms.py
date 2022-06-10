from django import forms
from formapp.models import Contents

class ContentsForm(forms.ModelForm):
    content = forms.CharField(max_length=20)
    class Meta:
        model = Contents
        fields = ("content",)