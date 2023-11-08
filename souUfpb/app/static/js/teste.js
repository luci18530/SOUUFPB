var pagina = document.currentScript.getAttribute('pg');
const csrf_token = document.currentScript.getAttribute('token');

// Função para salvar as seleções do usuário
function salvarSelecoes() {
    for (let i = 5 * pagina - 4; i <= 5 * pagina; i++) {
        const selecoes = {};
        const opcoes = document.querySelectorAll('[name="' + i + '"]:checked');
        opcoes.forEach((opcao) => {
            selecoes[opcao.name] = opcao.value;
        });
        sessionStorage.setItem('selecoes_' + i, JSON.stringify(selecoes));
    }
}

// Função para carregar as seleções do usuário
function carregarSelecoes() {
    for (let i = 5*pagina - 4; i <= 5*pagina; i++) {
        const selecoesSalvas = sessionStorage.getItem('selecoes_' + i);
        if (selecoesSalvas) {
            const selecoes = JSON.parse(selecoesSalvas);
            for (const name in selecoes) {
                const opcao = document.querySelector('[name="' + name + '"][value="' + selecoes[name] + '"]');
                if (opcao) {
                    opcao.checked = true;
                }
            }
        }
    }
}

function verificarRespostas() {
    var total = 0;
    for (let i = 1; i <= 30; i++) {
        const selecoesSalvas = sessionStorage.getItem('selecoes_' + i);
        if (selecoesSalvas) {
            total++;
        }
    }
    if (total == 30) return true;
    return false;
}

document.addEventListener('DOMContentLoaded', () => {
    // Carrega as seleções ao carregar a página
    carregarSelecoes();
    
    // Aguarda eventos de clique nos botões da paginação
    const botoesPaginacao = document.querySelectorAll('.pagination a.page-link');
    botoesPaginacao.forEach((botao) => {
        botao.addEventListener('click', () => {
            salvarSelecoes();
        });
    });
    
    // Aguarda evento de clique no botão de enviar
    const botaoEnviar = document.querySelector('#enviar');
    botaoEnviar.addEventListener('click', () => {
        salvarSelecoes();
        console.log(sessionStorage.length);
        if (verificarRespostas()) {
            
            var perguntas = JSON.parse(document.getElementById('perguntas').getAttribute('perguntas'));

            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/salvar_respostas/', true);
            xhr.setRequestHeader('X-CSRFToken', csrf_token); 

            var data = {'exatas': 0, 'biologicas': 0, 'engenharias': 0, 'saude': 0,
            'agrarias': 0, 'linguistica': 0, 'sociais': 0, 'humanas': 0}; 
            
            for (let i = 1; i <= 30; i++) {
                const selecoesSalvas = sessionStorage.getItem('selecoes_' + i);
                if (selecoesSalvas) {
                    const selecoes = JSON.parse(selecoesSalvas);
                    for (const name in selecoes) {
                        let value = Number(selecoes[name]);
                        data['exatas'] += value*perguntas[i-1].exatas;
                        data['biologicas'] += value*perguntas[i-1].biologicas;
                        data['engenharias'] += value*perguntas[i-1].engenharias;
                        data['saude'] += value*perguntas[i-1].saude;
                        data['agrarias'] += value*perguntas[i-1].agrarias;
                        data['linguistica'] += value*perguntas[i-1].linguistica;
                        data['sociais'] += value*perguntas[i-1].sociais;
                        data['humanas'] += value*perguntas[i-1].humanas;
                    }
                }
            }

            var menor = Math.min(data['exatas'], data['biologicas'], data['engenharias'], data['saude'],
            data['agrarias'], data['linguistica'], data['sociais'], data['humanas']);
            if (menor < 0) {
                data['exatas'] -= menor;
                data['biologicas'] -= menor;
                data['engenharias'] -= menor;
                data['saude'] -= menor;
                data['agrarias'] -= menor;
                data['linguistica'] -= menor;
                data['sociais'] -= menor;
                data['humanas'] -= menor;
            }

            xhr.send(JSON.stringify(data));
            xhr.onload = function () {
                if (xhr.status === 200) {
                    window.location.href = '/perfil/';
                }
            };
        }
        else {
            const alerta = document.getElementById('alerta');
            alerta.style.display = 'flex';
        }
    });

});
