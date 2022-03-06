from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


# Create your views here.

# pure python func
# - called with a django request object
# - returns django response object
from django_101.web.models import Todo


def index(request):
    context = {
        'title': 'function based view',
    }

    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'class based view',
        }

        return render(request, 'index.html', context)


class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'class based with TemplateView'
        return context


class TodosListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'
    ordering = ('title', 'category__name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My TODOs'

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        title_filter = self.request.GET.get('filter', None)

        if title_filter:
            queryset = queryset.filter(title__contains=title_filter)

        return queryset


class TodoDetailView(views.DetailView):
    model = Todo
    template_name = 'todo-detail.html'


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')
    fields = ('title', 'description', 'category')


# class RedirectToIndexView(views.RedirectView):
#     url = reverse_lazy('index class-based')
