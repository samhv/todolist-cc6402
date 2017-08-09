from django import forms

class AddTaskForm(forms.Form):
    description = forms.CharField(label="description", max_length=256, widget=forms.Textarea)
