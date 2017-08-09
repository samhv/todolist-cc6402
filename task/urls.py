from django.conf.urls import url

from task import views

urlpatterns = [
    url(r'^tasks', views.TaskView.as_view(), name="tasks")
]
