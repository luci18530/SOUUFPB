from django.core.management.base import BaseCommand
from app.models import Curso, Disciplina, RelacaoDisciplinas, Area, Pergunta
import json

def salvarCurso(item):
    try:
        curso = Curso.objects.get(nome = item['curso'])
    except Curso.DoesNotExist:
        area = Area.objects.get(nome = item['area'])
        curso = Curso.objects.create(nome = item['curso'],area = area, numPeriodos = len(item['periodos'])-1, chMinima = int(item['chMinima']))
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

        with open('app\management\commands\\areas.json', 'r',  encoding='utf-8') as file:
            data = json.load(file)
        
        for item in data['areas']:
            try:
                area = Area.objects.get(nome = item['nome'])
            except Area.DoesNotExist:
                area = Area.objects.create(nome = item['nome'],descricao = item['descricao'])
                area.save()

        self.stdout.write(self.style.SUCCESS('Áreas do conhecimento - OK'))

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

        self.stdout.write(self.style.SUCCESS('Cursos e disciplinas - OK'))

        with open('app\management\commands\\teste.json', 'r',  encoding='utf-8') as file:
            data = json.load(file)
        
        for item in data['questoes']:
            try:
                pergunta = Pergunta.objects.get(pergunta = item['pergunta'])
            except Pergunta.DoesNotExist:

                pergunta = Pergunta.objects.create(pergunta = item['pergunta'],exatas = item['exatas'],\
                biologicas = item['biologicas'], engenharias = item['engenharias'], saude = item['saude'],\
                agrarias = item['agrarias'], linguistica = item['linguistica'], sociais = item['sociais'],\
                humanas = item['humanas'] )

                pergunta.save()

        self.stdout.write(self.style.SUCCESS('Teste vocacional - OK'))
        self.stdout.write(self.style.SUCCESS('Banco de dados preenchido com sucesso!'))

