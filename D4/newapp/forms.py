from django.forms import ModelForm
from .models import New


class NewForm(ModelForm):

    class Meta:
        model = New
        fields = ['title', 'text']

