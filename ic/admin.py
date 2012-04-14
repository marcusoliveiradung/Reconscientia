# _*_ coding: utf8 _*_


from django.contrib import admin

from ic.models.projetoatividade import Evento, TipoAtividade, Projeto,\
     FaseProjeto, Participacao, FuncaoAtividade #, Utilizacao_Conteudo
from ic.models.conscin import AssocConscin, Conscin, TipoAssocConscin, AssocConscin_Area
from ic.models.conteudo import Conteudo, TipoConteudo #, Conteudo_Area
from ic.models.base import Area

#TIPOASSOCCONSCIN ADMIN
class AssocConscinInline(admin.TabularInline):
#     fieldsets = [
#     (None,{'fields': ['descricao']}),
#     ]
    model = AssocConscin

class TipoAssocConscinAdmin(admin.ModelAdmin):
    model = TipoAssocConscin
    inlines = [AssocConscinInline]
    extra = 7

class EventoInline(admin.TabularInline):
#     fieldsets = [
#     (None,{'fields': ['descricao']}),
#     ]
    model = Evento

#**********************************
class EventoAdmin(admin.ModelAdmin):
#     fieldsets = [
#     (None,{'fields': ['descricao']}),
#     ]
    model = Evento
    inlines = [EventoInline]
    extra = 4


class TipoAtividadeAdmin(admin.ModelAdmin):
#    fieldsets = [ 
#     ('Equipe', {'fields': ['equipe_atividade'], 'classes':['collapse']}),
#     ]
    model = TipoAtividade
    inlines = [EventoInline]
    extra = 3

class ParticipacaoInline(admin.StackedInline):
    model = Participacao
   

class AssocConscinAdmin(admin.ModelAdmin):
    model = AssocConscin
    inlines = [ParticipacaoInline]
    extra= 7 

class Arealine(admin.TabularInline):
    model = Area
    extra = 4

class AreaAdmin(admin.ModelAdmin):#     fieldsets = [ 
#     ('IC', {'fields': ['ic'], }),
#     ]
    model = Area
    inlines = [Arealine]
    extra = 10
    



class FaseInline(admin.TabularInline):
    model = FaseProjeto
    extra = 4


class ProjetoAdmin(admin.ModelAdmin):
    model = Projeto
    inlines = [FaseInline]
    extra = 3

class ProjetoInline(admin.TabularInline):
    model = Projeto
    extra = 3

class AreaProjetoAdmin(admin.ModelAdmin):
    model = Area
    inlines = [ProjetoInline]
    extra = 3

class ConteudoInline(admin.TabularInline):
    model = Conteudo
    extra = 3

class TipoConteudoAdmin(admin.ModelAdmin):
    model = TipoConteudo
    inlines = [ConteudoInline]
    extra = 3

admin.site.register(Conscin)
admin.site.register(TipoAssocConscin, TipoAssocConscinAdmin)
admin.site.register(AssocConscin, AssocConscinAdmin) 
admin.site.register(AssocConscin_Area) 
admin.site.register(Area, AreaAdmin)
admin.site.register(TipoAtividade, TipoAtividadeAdmin)
admin.site.register(FuncaoAtividade)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Participacao)
#admin.site.register(Utilizacao_Conteudo)
admin.site.register(TipoConteudo, TipoConteudoAdmin)
admin.site.register(Conteudo)
#admin.site.register(Conteudo_Area)
admin.site.register(Projeto, ProjetoAdmin)

#********************************
#Exs:
#fieldsets = [
        #(None, {'fields': ['id']}),
        #('Artefato', {'fields': ['artefato']}),
        #('Conteudo', {'fields': ['conteudo'], 'classes': ['collapse']})]
        #('Arquivo_Associado',        {'fields': ['foto.name']}), 


