from django.shortcuts import render
from django.views import generic as views


# Create your views here.
from tests_demo.web.models import Profile


class ProfileCreateView(views.CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profiles/create.html'


class ProfileListView(views.ListView):
    model = Profile
    template_name = 'profiles/list.html'


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profiles/details.html'
