from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    area = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(
        max_length=25,
        choices=(
            ('discordo_totalmente', '1'),
            ('discordo_parcialmente', '2'),
            ('neutro', '3'),
            ('concordo_parcialmente', '4'),
            ('concordo_totalmente', '5'),
        )
    )
    
    def __str__(self):
        return self.choice

class Curso(models.Model):

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
    
class Pergunta(models.Model):
    descricao = models.CharField(max_length=250)
    opcao_1 = models.CharField(default='Nada interessado', editable=False)
    opcao_2 = models.CharField(default='Pouco interessado', editable=False)
    opcao_3 = models.CharField(default='Neutro', editable=False)
    opcao_4 = models.CharField(default='Interessado', editable=False)
    opcao_5 = models.CharField(default='Muito interessado', editable=False)

    def __str__(self):
        return self.descricao