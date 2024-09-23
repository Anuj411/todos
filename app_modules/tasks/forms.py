from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("title", "description", "due_date")
        widgets={
            'due_date' : forms.TextInput(attrs={'type':'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = visible.field.label


class UpdateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"
        widgets={
            'due_date' : forms.TextInput(attrs={'type':'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = visible.field.label