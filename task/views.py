# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.base import TemplateView  
from django.views.generic.edit import DeleteView
from task.forms import AddTaskForm, DeleteTaskForm
from task.models import Task


class TaskView(TemplateView):
    template_name = "task/task_template.html"

    def get_context_data(self, **kwargs):
        context = {}
        form = AddTaskForm()
        context["form"] = form
        context["Tasks"] = Task.objects.all()
        context["formTaskList"] = DeleteTaskForm()
        return context

    def post(self, request):
        print(request.POST)
        #description = request.POST.get("description")
        #Task.objects.create(description=description)
        return redirect("tasks")
        
class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:all')
