from django import forms
from todo.models import ToDo

class ToDoForm(forms.Form):
    todo_text = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                        'placeholder':'Add Your Todo'}))

    
    # def cleaned_data(self.*args,**kwargs):
    #     pass