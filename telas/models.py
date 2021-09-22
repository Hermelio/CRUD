from django.db import models


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=40)
    cpf = models.CharField('Cpf', max_length=15)
    status = models.BooleanField('Status', default=True)
    telefone = models.CharField('Telefone', max_length=15)
    email = models.EmailField('Email')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nome} - Telefone = {self.telefone}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
