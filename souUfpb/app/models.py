from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):

    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
    
class Pergunta(models.Model):

    pergunta = models.CharField(max_length=200)

    exatas = models.IntegerField(default=0)
    biologicas = models.IntegerField(default=0)
    engenharias = models.IntegerField(default=0)
    saude = models.IntegerField(default=0)
    agrarias = models.IntegerField(default=0)
    linguistica = models.IntegerField(default=0)
    sociais = models.IntegerField(default=0)
    humanas = models.IntegerField(default=0)

    def __str__(self):
        return self.pergunta

# class Escolha(models.Model):
#     pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
#     escolha = models.CharField(
#         max_length=25,
#         choices=(
#             ('discordo_totalmente', '1'),
#             ('discordo_parcialmente', '2'),
#             ('neutro', '3'),
#             ('concordo_parcialmente', '4'),
#             ('concordo_totalmente', '5'),
#         )
#     )
    
#     def __str__(self):
#         return self.escolha

class Curso(models.Model):

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    nome = models.CharField(max_length=128)
    numPeriodos = models.IntegerField()
    chMinima = models.IntegerField()

    def __str__(self):
        return self.nome 
    
class Disciplina(models.Model):

    codigo = models.CharField(primary_key=True, max_length=32)
    nome = models.CharField(max_length=128)
    carga = models.IntegerField()

    def __str__(self):
        return self.codigo
    
class RelacaoDisciplinas(models.Model):

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    periodo = models.IntegerField()

    def __str__(self):
        return f'{self.curso.nome} - {self.periodo}º período - {self.disciplina.codigo}'

    
class Resultado(models.Model):

    exatas = models.IntegerField(default=0)
    biologicas = models.IntegerField(default=0)
    engenharias = models.IntegerField(default=0)
    saude = models.IntegerField(default=0)
    agrarias = models.IntegerField(default=0)
    linguistica = models.IntegerField(default=0)
    sociais = models.IntegerField(default=0)
    humanas = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)