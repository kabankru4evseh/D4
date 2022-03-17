from django.shortcuts import render
from django.views.generic import ListView
from .models import New
from django.core.paginator import Paginator
from .filters import NewFilter, F
from django.contrib.auth.models import User
from .forms import NewForm


class NewList(ListView):
    model = New
    template_name = 'new_list.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 1
    form_class = NewForm

    def get_filter(self):
        return NewFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
            }


def user_list(request):
    f = F(request.GET, queryset=User.objects.all())
    return render(request, 'user_t.html', {'filter': f})


def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)

