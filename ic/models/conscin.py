#-*- coding: utf-8 -*-

from django.db import models

class Conscin(models.Model):
    nome = models.CharField(max_length=200) 
    data_nascimento = models.DateField('Data de Nascimento', blank= 'True', null='True')
    email = models.EmailField( blank= 'True', null='True')
    tel_resid = models.CharField("Telefone Residencial", max_length=20,blank= 'True', null='True')
    tel_cel = models.CharField("Telefone Celular", max_length=20, blank= 'True', null='True')
    tel_cel_2 = models.CharField("Telefone Celular 2", max_length=20, blank= 'True', null='True')    
    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'ic'





 
 
        
        
        

#    data_desligamento = models.DateField()
#    motivo_desligamento = models.TextField(Area, blank='True', null='True')
#
#    def __unicode__(self):
#        return self.voluntario














    

