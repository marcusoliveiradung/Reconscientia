# _*_ coding: utf8 _*_

from django.db import models
from django.core.files import File


class Conscin(models.Model):  
    nome = models.CharField(max_length=200) 
    data_nascimento = models.DateField('Data de Nascimento:', blank= 'True', null='True')
    email = models.EmailField()
    tel_resid = models.CharField(max_length=20,blank= 'True', null='True')
    tel_cel = models.CharField(max_length=20, blank= 'True', null='True')
    def __unicode__(self):
        return self.nome
#    nome = models.CharField(max_length=200)  
    #((interelacao_consciencial= models.ForeignKey('self', related_name = 'conscin_relacionada', blank= 'True', null='True')


#################################################################################
# IL : (CLASSES INTERNAS)
#*)Subdivisão de/para EMPRESA
class Area(models.Model):
    nome = models.CharField(max_length=200)  
    descricao = models.TextField()   
    area_sup= models.ForeignKey('self', related_name = 'area_sup_self', blank= 'True', null='True')
    def __unicode__(self):
        return self.nome

class Voluntario_ou_Associado(models.Model):
    #nome = models.CharField(max_length=200) 
    #data_nascimento = models.DateField('Data de Nascimento:', blank= 'True', null='True')
    #email = models.EmailField()
    #tel_resid = models.CharField(max_length=20,blank= 'True' )
    #tel_cel = models.CharField(max_length=20)
    ind_tenepes = models.NullBooleanField()
    ind_docencia =  models.NullBooleanField()
    obs_docencia = models.TextField(blank= 'True')
    conscin =  models.ForeignKey(Conscin, blank= 'True', null='True')
    area_trabalho =  models.ManyToManyField(Area,blank= 'True', null='True')

    def __unicode__(self):
        return self.conscin.nome



#########################################################################################################################################


class Tipo_Conteudo(models.Model):
    """ Classificação de conteúdo como por ex.ATA, PLANO PERiODICO, RASCUNHO, LISTA PRESENCA ETC
    """
    nome = models.CharField(max_length=200) 
    descricao = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nome

#(SUPER_TIPO_ATIVIDADE

########################################################################################################################################
#CLASSES BASICAS DE DOMINIO SECUNDARIO ( já com objetos operacionais )

#*)(TIPO_)ATIVIDADE-SERVICO: Classificação de ATIVIDADES ou SERVICOS como por ex. FACILIT_PESQ ( RECONSCIENTIA), CINECLUBE ( DISCERNIEMNTUM), MANUTENC_HW&SW(CEAEC-HOLOCICLO-INF) ETC 
class Tipo_Atividade(models.Model):#ou Servico(s)
    nome = models.CharField(max_length=200) 
    descricao = models.CharField(max_length=300)  
    ind_int_ext =  models.NullBooleanField()
    duracao_horas= models.IntegerField(blank= 'True', null='True' )
    prioridade= models.IntegerField(blank= 'True', null='True')
    tipo_atividade_sup= models.ForeignKey('self', related_name = 'tipo_ativ_sup', blank= 'True', null='True')
    equipe_atividade = models.ManyToManyField(Voluntario_ou_Associado,blank= 'True', null='True')
    resp_atividade = models.ManyToManyField(Area,blank= 'True', null='True')
    #FK para Classe, TIPo ou Categoria de ATIVIDADE ou SERVICO ( caso haja 1 classe de tipologia real dos tipos de atividades)
    def __unicode__(self):
        return self.nome    

#*)CLASSE PARA PROJETO(S) EM GERAL 
class Projeto(models.Model):
    nome = models.CharField(max_length=500) 
    descricao = models.TextField()
    data_inicial = models.DateTimeField('Data Inicial do Projeto:')
    duracao_meses= models.IntegerField()
    prioridade= models.IntegerField()
    area = models.ManyToManyField(Area, blank= 'True', null='True')
    tipo_atividade = models.ManyToManyField(Tipo_Atividade, blank= 'True', null='True')
    def __unicode__(self):
        return self.nome

#*)CLASSE materializada FASE (SUBPROJETO):
#Deve ser incorporada a Projeto (generalizacao)
class Fase(models.Model): 
    
    codigo_fase = models.CharField(max_length=100)  
    nome = models.CharField(max_length=500) 
    descricao = models.TextField()  
    data_inicial = models.DateTimeField('Data Inicial do Projeto:')
    duracao_dias= models.IntegerField()
    prioridade= models.IntegerField()
    projeto = models.ForeignKey(Projeto)
    fase_sup = models.ForeignKey('self')
    def __unicode__(self):
        return self.nome

###########################################################################################################################################
    
#CLASSE EQUIPE de-para determinada ATIVIDADE ( ou Servico), ou seja, Voluntário X Atividade ( Ex-Tipo de Atividade)
#IMP- Foi inibida pela utilização do recurso de relacionamento NxM, desde a classe de Atividade-Servico ( Ex-Tipo_Atividade)
#class Equipe(models.Model):

    #nome = models.CharField(max_length=200) 
    #funcao = models.CharField(max_length=200) 
    #tipo_atividade = models.ForeignKey(Tipo_Atividade)
    #voluntario = models.ForeignKey(Voluntario)  
    #def __unicode__(self):
         #return self.funcao


#*)CONTEUDO ( PRODUCAO-PRODUTO de CONTEUDO) em SI:
class Conteudo(models.Model):

    tipo_conteudo = models.ForeignKey(Tipo_Conteudo)    
    nome = models.CharField(max_length=100) 
    descricao = models.CharField(max_length=200)
    conteudo = models.FileField(upload_to ='Documentos',blank= 'True', null='True')
    #FK ( Logica por enquanto para PESSOA ou PESSOA/CONSCIN.VOLUNTARIO )
    def __unicode__(self):
        return self.nome
    


#*)CLASSE  ATIVIDADE ( Envento em si ou Ocorrência da Atividade) 
class Agenda(models.Model):
   
    descricao  = models.CharField(max_length=200) 
    data_hora_ini = models.DateTimeField('data e hora inicial')
    data_hora_fim = models.DateTimeField('date e hora final')
    descricao = models.CharField(max_length=300)  
    tipo_atividade = models.ForeignKey(Tipo_Atividade)
    projeto_rel = models.ManyToManyField(Projeto,blank= 'True', null='True') 
    work_team_extra = models.ManyToManyField(Voluntario_ou_Associado) 
    producao = models.ManyToManyField(Conteudo,blank= 'True', null='True') #avaliar dependencia a Conteudo
    def __unicode__(self):
        return self.descricao
    #def __unicode__(self):
    #    data_hora =  datetime() 
    #    return self.data_hora



    
