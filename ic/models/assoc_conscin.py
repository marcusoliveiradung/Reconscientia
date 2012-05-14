#-*- coding: utf-8 -*-

from django.db import models

from ic.models.conscin import Conscin
from ic.models.emp import Area

class TipoAssocConscin(models.Model):
    nome = models.CharField(max_length=200)  
    descricao = models.TextField()   

    def __unicode__(self):
        return self.nome
    
    class Meta:
        app_label = 'ic'

class AssocConscin(models.Model):
    conscin =  models.ForeignKey(Conscin, blank='True', null='True')
    ind_tenepes = models.NullBooleanField()
    ind_docencia = models.NullBooleanField()
    obs_docencia = models.TextField(blank='True')    
    tipo_assoc_conscin = models.ForeignKey(TipoAssocConscin)
    area_trabalho =  models.ManyToManyField(Area,blank='True', null='True') #through = "AssocConscin_Area",
                                             

    def __unicode__(self):
        return self.conscin.nome

    class Meta:
        app_label = 'ic'


#class AssocConscin_Area(models.Model):
#    assocconscin = models.ForeignKey(AssocConscin)
#    area = models.ForeignKey(Area)  
     
#    def __unicode__(self):
#        return self.
       
#    class Meta:
#        app_label = 'ic'
#        
