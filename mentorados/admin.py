from django.contrib import admin
from .models import Mentorados, Navigators, Reuniao, DisponibilidadeHorarios

admin.site.register(Navigators)
admin.site.register(Mentorados)
admin.site.register(Reuniao)
admin.site.register(DisponibilidadeHorarios)