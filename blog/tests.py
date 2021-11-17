from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
# Create your tests here.
from django.views.generic import ListView
from .models import Task
