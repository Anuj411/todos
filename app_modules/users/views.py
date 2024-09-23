from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View
from .forms import LoginForm, RegisterForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from app_modules.tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
User = get_user_model()


class LoginView(TemplateView):
    template_name = "users/login.html"
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm()
        return context

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse("users:dashboard"))
        return render(self.request, self.template_name, {"form": LoginForm(), "error": "Login credentials are incorrect !!!"})


class LogoutView(View):
    def get(self, request):
        logout(self.request)
        return HttpResponseRedirect(reverse("users:login"))


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse("users:login"))

    def form_invalid(self, form):
        return super().form_invalid(form)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "users/dashboard.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object_list"] = Task.objects.all()
        return context