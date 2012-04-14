#-*- coding: utf-8 -*-

from django.db import models
from ic.models.base import Area


class Conscin(models.Model):
    nome = models.CharField(max_length=200) 
    data_nascimento = models.DateField('Data de Nascimento', blank= 'True', null='True')
    email = models.EmailField()
    tel_resid = models.CharField("Telefone Residencial", max_length=20,blank= 'True', null='True')
    tel_cel = models.CharField("Telefone Celular", max_length=20, blank= 'True', null='True')
    
    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'ic'


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
    area_trabalho =  models.ManyToManyField(Area,through = "AssocConscin_Area",
                                             blank='True', null='True')

    def __unicode__(self):
        return self.conscin.nome

    class Meta:
        app_label = 'ic'


class AssocConscin_Area(models.Model):
    assocconscin = models.ForeignKey(AssocConscin)
    area = models.ForeignKey(Area)  
     
#    def __unicode__(self):
#        return self.
       
    class Meta:
        app_label = 'ic'
        
 
 
        
        
        

#    data_desligamento = models.DateField()
#    motivo_desligamento = models.TextField(Area, blank='True', null='True')
#
#    def __unicode__(self):
#        return self.voluntario














    

