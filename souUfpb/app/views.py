from django.shortcuts import get_object_or_404, render
from .models import Question, Choice, Curso, RelacaoDisciplinas, Disciplina
from .forms import QuestionarioForm
from .forms import SignupForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.db.models import F
from django.http import JsonResponse

def get_data(request):
    curso_id = request.GET.get('id', '')
    if curso_id:
        listaDiscPeriodos = []
        for i in range (get_object_or_404(Curso, pk=curso_id).numPeriodos + 1):
            listaCodigos = RelacaoDisciplinas.objects.filter(curso = curso_id, periodo = i).values_list('disciplina', flat=True)
            listaDisciplinas = []
            for cod in listaCodigos:
                disc = get_object_or_404(Disciplina, codigo=cod)
                listaDisciplinas.append(cod + ' - ' + disc.nome + ' - ' + str(disc.carga) +'CH')

            listaDiscPeriodos.append(listaDisciplinas)
        return JsonResponse({'dados': listaDiscPeriodos})
    
    return render(request, 'app/not_authorized.html')

@login_required
def teste(request):
    perguntas = Question.objects.all()
    if request.method == 'POST':
        form = QuestionarioForm(request.POST, perguntas=perguntas)
        if form.is_valid():
            # Processar as respostas aqui
            for pergunta in perguntas:
                texto_resposta = form.cleaned_data[f'pergunta_{pergunta.id}']
                Choice.objects.create(pergunta=pergunta, texto=texto_resposta)
    else:
        form = QuestionarioForm(perguntas=perguntas)
    return render(request, 'app/teste.html', {'form': form, 'page': 'teste'})

@login_required
def cursos(request):
    listaCursos = Curso.objects.all()
    query = request.GET.get('query', '')

    if query:
        # Use a função unaccent para remover a acentuação e crie um campo virtual
        listaCursos = listaCursos.annotate(nome_unaccent=F("nome"))
        
        # Realize a filtragem no campo virtual com a função unaccent
        listaCursos = listaCursos.extra(
            where=["unaccent(nome::text) ILIKE unaccent(%s)"],
            params=['%' + query + '%']
        )

    listaCursos = listaCursos.order_by('nome')

    return render(request, 'app/cursos.html', {'lista': listaCursos, 'page': 'cursos'})

@login_required
def detalhes_curso(request, curso_id):
     curso = get_object_or_404(Curso, pk=curso_id)
     return render(request, 'app/detalhes_curso.html', {'curso': curso, 'page': 'cursos'})

@login_required
def home(request):
    return render(request, 'app/home.html', {'page': 'home'})

@login_required
def perfil(request):
    return render(request, 'app/perfil.html', {'page': 'perfil'})

def inicial(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    else:
        form = SignupForm()
    
    return render(request, 'app/inicial.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Verifica se há uma URL de redirecionamento na consulta GET
            next_url = request.GET.get('next')
            if next_url:
                # Redireciona o usuário para a URL de redirecionamento
                return redirect(next_url)
            else:
                # Redireciona o usuário para a página padrão após o login
                return redirect('app:home')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    else:
        form = SignupForm()
    return render(request, 'app/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('app:inicial')

