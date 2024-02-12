from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Profile
from typing import Any
from django.shortcuts import render
from .forms import ProfileForm
from django.views.generic import TemplateView, CreateView

# Create your views here.
class ProfileCreation(CreateView):
    template_name = "resume_gen/accept.html"
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("resume-create")