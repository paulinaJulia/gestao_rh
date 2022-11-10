from django.db import models
from funcionarios.models import Funcionario
class RegistroHoraExtra(models.Model):

    motivo = models.CharField(
        max_length=100,
    )
    #funcionario com registro de hora extra
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.motivo
        
