#-*- coding: utf-8 -*-

from django.db import models
from ic.models.base import Area
from ic.models.conteudo import Conteudo
from ic.models.conscin import AssocConscin


class TipoAtividade(models.Model):
    """ 
    Ex: Facilitacao de Pesquisa, Motivacao-Trabalho-Lazer,
    Reuniao Geral
    
    Pode conter sub-atividades (campo tipo_atividade_sup)
    """
    nome = models.CharField(max_length=200) 
    descricao = models.CharField(max_length=300)  
    ind_int_ext = models.NullBooleanField()
    duracao_horas= models.IntegerField(blank='True', null='True' )
    prioridade= models.IntegerField(blank='True', null='True')
    tipo_atividade_sup = models.ForeignKey('self', related_name = 'tipo_ativ_sup', blank= 'True', null='True')
    equipe_atividade = models.ManyToManyField(AssocConscin, blank='True', null='True')
    area_resp = models.ManyToManyField(Area, blank='True', null='True')

    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'ic'


class Projeto(models.Model):
    """ Conjunto de atividades que tem uma data para acabar """
    
    nome = models.CharField(max_length=500) 
    descricao = models.TextField()
    inicio = models.DateTimeField('Inicio')
    duracao_meses = models.IntegerField()
    prioridade = models.IntegerField()
    area = models.ManyToManyField(Area, blank='True', null='True')
    tipo_atividade = models.ManyToManyField(TipoAtividade, blank='True', null='True')

    def __unicode__(self):
        return self.nome


    class Meta:
        app_label = 'ic'


class FuncaoAtividade(models.Model):
    tipo_atividade = models.ForeignKey(TipoAtividade)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __unicode__(self):
        return self.nome
    

    class Meta:
        app_label = 'ic'


class FaseProjeto(models.Model): 
    """ Fase de um projeto. Ex: 
    
    """
    codigo_fase = models.CharField(max_length=100)  
    nome = models.CharField(max_length=500) 
    descricao = models.TextField()  
    inicio = models.DateTimeField('Inicio')
    fim = models.DateTimeField('Fim')
    projeto = models.ForeignKey(Projeto)
    fase_projeto_sup = models.ForeignKey('self', blank= 'True', null='True')
    
    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'ic'


class Evento(models.Model):
    """ Evento em si ou Ocorrencia da Atividade """
    
    descricao = models.CharField(max_length=200) 
    inicio = models.DateTimeField('Inicio')
    fim = models.DateTimeField('Fim')
    descricao = models.CharField(max_length=300)
    tipo_atividade = models.ForeignKey(TipoAtividade)
    atividade_projeto_sup = models.ForeignKey('self', blank= 'True', null='True') 
    area = models.ManyToManyField(Area,blank= 'True', null='True')
    projeto = models.ManyToManyField(Projeto, blank= 'True', null='True')
    assoc_conscin = models.ManyToManyField(AssocConscin, through="Participacao")  
    producao = models.ManyToManyField(Conteudo, blank= 'True', null='True') #avaliar dependencia a Conteudo
 
    def __unicode__(self):
        return self.descricao
   
    class Meta:
        app_label = 'ic'

 
class Participacao(models.Model):
    evento = models.ForeignKey(Evento)
    area = models.ForeignKey(Area)
    assoc_conscin = models.ForeignKey(AssocConscin)
    funcao = models.ForeignKey(FuncaoAtividade, blank=True, null=True)
    ind_pagto = models.NullBooleanField(blank=True, null=True)
    valor_pago = models.IntegerField(blank=True, null=True)
    ind_presenca = models.NullBooleanField(blank=True, null=True)
    percentual_presenca = models.SmallIntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.evento.descricao
    
    class Meta:
        app_label = 'ic'

 
    
