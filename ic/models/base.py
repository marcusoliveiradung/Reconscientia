

from django.db import models

from ic.models.assoc_conscin import AssocConscin
from ic.models.emp import Area


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

class FuncaoAtividade(models.Model):
    tipo_atividade = models.ForeignKey(TipoAtividade)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __unicode__(self):
        return self.nome
    

    class Meta:
        app_label = 'ic'

class FormaPagto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __unicode__(self):
        return self.nome
    
    class Meta:
        app_label = 'ic'



    
    