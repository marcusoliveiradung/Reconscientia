

from django.db import models

class Area(models.Model):
    """ Ex: Banco de Dados, Comunicacao etc.. 
    
    Pode conter sub-areas (campo area_sup)
    """
    nome = models.CharField(max_length=200)  
    descricao = models.TextField()   
    area_sup= models.ForeignKey('self', related_name = 'area_sup_self', 
                                blank= 'True', null='True')
    
    
    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'ic'


    
    