from datetime import time
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def cpf_check(cpf):
    status = True
    if len(cpf) != 11:
        status = False
    for c in cpf:
        if c.isnumeric() == False:
            status = False
    return status

def cpf_val(cpf):
    if cpf_check(cpf) == True:
        return cpf
    else:
        raise ValidationError('CPF inválido')
    

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, validators=[cpf_val])
    register_date = models.DateField()
    
    def __str__(self):
        return self.name



# Create your models here.
