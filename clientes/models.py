from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    razao_social = models.CharField(max_length=255, verbose_name="Razão Social")
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    email = models.EmailField(verbose_name="E-mail de Contato")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.razao_social