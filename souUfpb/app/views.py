from django.shortcuts import get_object_or_404, render
from .models import Question, Choice, Curso
from .forms import QuestionarioForm
from .forms import SignupForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.db.models import F


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

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Se for uma solicitação AJAX, retorne apenas o HTML da lista
        cursos_html = '\n'.join([f'<p><a href="{reverse("app:detalhes_curso", args=[curso.id])}">{curso.nome}</a></p>' for curso in listaCursos])
        return HttpResponse(cursos_html, content_type='text/html')
    else:
        # Caso contrário, renderize a página completa
        return render(request, 'app/cursos.html', {'lista': listaCursos, 'page': 'cursos'})

def detalhes_curso(request, curso_id):
     curso = get_object_or_404(Curso, pk=curso_id)
     return render(request, 'app/detalhes_curso.html', {'curso': curso})

def home(request):
    return render(request, 'app/home.html', {'page': 'home'})

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
    return redirect('app:home')

