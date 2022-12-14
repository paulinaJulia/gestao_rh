from enum import unique
from django.db import models
from django.contrib.auth.models import User
from departamentos.models import Departamento
from empresa.models import Empresa
class Funcionario(models.Model):
    
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome',
    )

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True
       
    )
    #Lista de departamentos
    departamentos = models.ManyToManyField(Departamento)
    #empresa a qual o funcionario pertence
    
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.PROTECT,
    )


    def __str__(self):
        return self.nome