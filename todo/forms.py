from django import forms
from .models import *

class TodoForm(forms.ModelForm):
    class Meta:
        model =Todo
        fields = "__all__"
        labels = {
        'title':'Title',
         'description':'Description',
         'status':'Status',
         'priority':'Priority',

 }

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control row mb-3', 'placeholder':'Title'})
        }