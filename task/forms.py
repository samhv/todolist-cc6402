from django import forms
from models import Task

class AddTaskForm(forms.Form):
    description = forms.CharField(label="description", max_length=256, widget=forms.Textarea)

class DeleteTaskForm(forms.Form):
    tasks = forms.ModelMultipleChoiceField(queryset=Task.objects.all().values_list("description", flat=True), label="Task List", widget=forms.CheckboxSelectMultiple())