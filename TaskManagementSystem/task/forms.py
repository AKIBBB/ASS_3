from django import forms
from .models import TaskModel

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_title', 'task_description', 'is_completed', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }
