from django.forms import ModelForm
from .models import Client
from django.utils import timezone


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'cpf']



# Create your models here.
