from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Task
from django.urls import reverse_lazy
class BlogListView(ListView):
    model = Task
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Task
    template_name = "post_detail.html"



class BlogCreateView(CreateView):
    model = Task
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Task
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Task
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
