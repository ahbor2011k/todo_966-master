from django import forms

from task.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=['title','description','is_done']
        widgets={
            "title": forms.TextInput(attrs={'class':'control'}),
            "description": forms.Textarea(attrs={'class': 'control'}),
            "is_done": forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }