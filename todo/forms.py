from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model =Todo
        fields = "__all__"
        exclude = ['user']
        labels = {
        'title':'Title',
         'description':'Description',
         'status':'Status',
         'priority':'Priority',

 }

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control row my-3', 'placeholder':'Title'}),
            'description':forms.Textarea(attrs={'class':'form-control row mb-3','placeholder':'Description', 'rows':6}),
            'status':forms.Select(attrs={"class":"form-select row mb-3"}),
            'priority':forms.Select(attrs={"class":"form-select row mb-3"})
        }