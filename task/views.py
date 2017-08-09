# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
# Create your views here.
from task.forms import AddTaskForm
from task.models import Task


class TaskView(TemplateView):
    template_name = "task/task_template.html"

    def get_context_data(self, **kwargs):
        context = {}
        form = AddTaskForm()
        context["form"] = form
        return context

    def post(self, request):
        description = request.POST.get("description")
        Task.objects.create(description=description)
        return redirect("tasks")