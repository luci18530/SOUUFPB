from django.contrib import admin

from .models import Curso, Disciplina, RelacaoDisciplinas, Pergunta, Area

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(RelacaoDisciplinas)
admin.site.register(Pergunta)
admin.site.register(Area)
