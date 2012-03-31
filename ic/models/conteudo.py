#-*- coding: utf-8 -*-

from django.db import models

class TipoConteudo(models.Model):
    """ Classificacao de conteudo 
    
    Ex: ATA, PLANO PERiODICO, RASCUNHO, LISTA PRESENCA ETC
    """
    nome = models.CharField(max_length=200) 
    descricao = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'ic'


class Conteudo(models.Model):
    """ Conteudo em si """
    
    tipo_conteudo = models.ForeignKey(TipoConteudo)    
    nome = models.CharField(max_length=100) 
    descricao = models.CharField(max_length=200)
    conteudo = models.FileField(upload_to = 'conteudo', blank= 'True', null='True')
    #FK ( Logica por enquanto para PESSOA ou PESSOA/CONSCIN.VOLUNTARIO )
    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'ic'
