from django_filters import FilterSet, CharFilter
from .models import New
from django.contrib.auth.models import User


class NewFilter(FilterSet):
    class Meta:
        model = New
        fields = {
            'title': ['icontains']
            # нужен фильтр по дате
        }


class F(FilterSet):
    username = CharFilter(method='my_filter')

    class Meta:
        model = User
        fields = ['username']

        def my_filter(self, queryset, name, value):
            return queryset.filter(**{
                name: value
            })
