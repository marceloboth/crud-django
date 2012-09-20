# -*- coding: utf-8 -*-
from django.db import models


class Cliente(models.Model):
    """
    Cadastro de clientes
    """
    nome = models.CharField(max_length=50)
    sobre_nome = models.CharField(max_length=50)
    data_nascimento = models.DateTimeField()
    profissao = models.ForeignKey('Profissao')

    def __unicode__(self):
        return self.nome


class Profissao(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = u'Profissão'
        verbose_name_plural = u'Profissões'

    def __unicode__(self):
    	return self.nome
