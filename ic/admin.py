from django.contrib import admin

# from portal_ic - app
from ic.models import  Tipo_Conteudo, Voluntario_ou_Associado, Tipo_Atividade, Agenda, Conteudo, Projeto, Area,Conscin, Fase


class AgendaInline(admin.TabularInline):
#     fieldsets = [
#     (None,{'fields': ['descricao']}),
#     ]
     model = Agenda
     extra = 4
class Tipo_AtividadeAdmin(admin.ModelAdmin):
#    fieldsets = [ 
#     ('Equipe', {'fields': ['equipe_atividade'], 'classes':['collapse']}),
#     ]
     model = Tipo_Atividade
     inlines = [AgendaInline]
     extra = 3

class VoluntarioAdmin(admin.ModelAdmin):
     model= Voluntario_ou_Associado
     inline = [AgendaInline]
     extra = 10
#***********************************
#class AreaAdmin(admin.ModelAdmin):
#     fieldsets = [ 
#     ('IC', {'fields': ['ic'], }),
#     ]
#     model= Area
#     extra=2
     
#***********************************
class FaseInline(admin.TabularInline):
     model = Fase
     extra = 4

class ProjetoAdmin(admin.ModelAdmin):
     model = Projeto
     inlines = [FaseInline]
     extra = 3
#************************************
class ConteudoInline(admin.TabularInline):
     model = Conteudo
     extra = 3

class Tipo_ConteudoAdmin(admin.ModelAdmin):
     model = Tipo_Conteudo
     inlines = [ConteudoInline]
     extra = 3

#********************************
admin.site.register(Conscin)
admin.site.register(Voluntario_ou_Associado, VoluntarioAdmin)
admin.site.register(Area)#, AreaAdmin)
admin.site.register(Tipo_Atividade,Tipo_AtividadeAdmin)
admin.site.register(Agenda)
admin.site.register(Tipo_Conteudo,Tipo_ConteudoAdmin)
admin.site.register(Conteudo)
admin.site.register(Projeto, ProjetoAdmin)
#admin.site.register(Fase)
#********************************
#fieldsets = [
        #(None, {'fields': ['id']}),
        #('Artefato', {'fields': ['artefato']}),
        #('Conteudo', {'fields': ['conteudo'], 'classes': ['collapse']})]
        #('Arquivo_Associado',        {'fields': ['foto.name']}), 



