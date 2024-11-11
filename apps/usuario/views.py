from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView ,TemplateView


# Create your views here.



class login(TemplateView):
    template_name = 'user/login.html'

