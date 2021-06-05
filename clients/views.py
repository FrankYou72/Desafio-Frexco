from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from .forms import ClientForm
from .models import Client
from django.utils import timezone
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        test_form = ClientForm(request.POST)
        error_message = test_form.errors
        if test_form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            cpf = request.POST['cpf']
            new_Client = Client(name = name, email = email, cpf = cpf, register_date = timezone.now())
            print(name, email, cpf)
            new_Client.save()
            messages.info(request, 'Client registered successfully')
            print('Foi')
        else:
            new_Client = ClientForm()
            print('Não foi')
    else:
        new_Client = ClientForm()
        error_message = ''

    return render(request, 'register.html', {
        'new_Client': new_Client,
        'error_message': error_message}
        )


def home(request):
    clients_list = Client.objects.order_by('-register_date')
    context = {
        'clients_list' : clients_list
    }
    return render(request, 'home.html', context)


# Create your views here.
