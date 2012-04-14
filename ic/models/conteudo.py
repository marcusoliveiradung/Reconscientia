#-*- coding: utf-8 -*-

from django.db import models


from ic.models.base import Area



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
    artefato_area = models.ManyToManyField(Area,blank='True',null='True') #through="Conteudo_Area",
                                                
    #uso_artefato = models.ManyToManyField(Evento, through= "Utilizacao_Conteudo")    
    conteudo = models.FileField(upload_to = 'conteudo') #, blank= 'True', null='True')
    #FK ( Logica por enquanto para PFESSOA ou PESSOA/CONSCIN.VOLUNTARIO )
    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'ic'
        

#class Conteudo_Area(models.Model):
#    
#    conteudo = models.ForeignKey(Conteudo,blank='True',null='True')
#    area = models.ForeignKey(Area)
   ##descricao = models.CharField(max_length=200)
    
 #   def __unicode__(self):
 #       return self.area.nome + ' / ' + self.conteudo.nome   
    
 #   class Meta:
 #       app_label = 'ic'
        

#    descricao = models.CharField(max_length=200)
#    xx = models.ManytoMany(Evento, through= "Utilização_Conteudo")
#    conteudo = models.FileField(upload_to = 'conteudo', blank= 'True', null='True')
    #FK ( Logica por enquanto para PESSOA ou PESSOA/CONSCIN.VOLUNTARIO )
#    def __unicode__(self):
#        return self.nome

   