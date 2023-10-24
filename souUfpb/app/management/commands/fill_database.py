from django.core.management.base import BaseCommand
from app.models import Curso, Disciplina, RelacaoDisciplinas
import json

def salvarCurso(item):
    try:
        curso = Curso.objects.get(nome = item['curso'])
    except Curso.DoesNotExist:
        curso = Curso.objects.create(nome = item['curso'],numPeriodos = len(item['periodos'])-1, chMinima = int(item['chMinima']))
        curso.save()
    return curso
    
def salvarDisciplina(componente):
    componente = [s.strip() for s in componente.split('-')]
    cod = componente.pop(0)
    carga = componente.pop().removesuffix('CH')
    nome = ' - '.join(componente)

    try:
        disciplina = Disciplina.objects.get(codigo = cod)
    except Disciplina.DoesNotExist:
        disciplina = Disciplina.objects.create(codigo = cod, nome = nome, carga = carga)
        disciplina.save()
    return disciplina

class Command(BaseCommand):
    help = 'Este é um comando personalizado do Django.'

    def handle(self, *args, **options):

        with open('app\management\commands\cursos.json', 'r',  encoding='utf-8') as file:
            data = json.load(file)

        for item in data['cursos']:

            curso = salvarCurso(item)

            for periodo, info in item['periodos'].items():
                for componente in info['componentes']:

                    disciplina = salvarDisciplina(componente)

                    relacao_disciplinas = RelacaoDisciplinas.objects.create(curso = curso,\
                    disciplina = disciplina, periodo = int(periodo.removesuffix('º Período')))

                    relacao_disciplinas.save()

        self.stdout.write(self.style.SUCCESS('Banco de dados preenchido com sucesso!'))

