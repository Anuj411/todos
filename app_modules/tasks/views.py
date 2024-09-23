from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, View
from .forms import CreateTaskForm, UpdateTaskForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class ListTaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list-task.html"


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = "tasks/create-task.html"
    form_class = CreateTaskForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse("tasks:list_task"))

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    
class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = "tasks/update-task.html"
    form_class = UpdateTaskForm
    model = Task

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse("tasks:list_task"))

    def form_invalid(self, form):
        return super().form_invalid(form)


class DeleteTaskView(LoginRequiredMixin, View):
    def get(self, request, pk):
        Task.objects.filter(id = pk).delete()
        return HttpResponseRedirect(reverse("tasks:list_task"))