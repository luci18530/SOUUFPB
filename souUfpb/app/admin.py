from django.contrib import admin

from .models import Question, Choice, Curso, Disciplina, RelacaoDisciplinas, Pergunta

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(RelacaoDisciplinas)
admin.site.register(Pergunta)
