var pagina = document.currentScript.getAttribute('pg');
const csrf_token = document.currentScript.getAttribute('token');
var perguntasData = [];

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
            for (pergunta in perguntasData) {
                console.log(pergunta);
            }
            
            // armazena as respostas e redireciona para perfil
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/salvar_respostas/', true);
            xhr.setRequestHeader('X-CSRFToken', csrf_token);  // Certifique-se de incluir o token CSRF

            var data = {'exatas': 0, 'biologicas': 0, 'engenharias': 0, 'saude': 0,
            'agrarias': 0, 'linguistica': 0, 'sociais': 0, 'humanas': 0}; 
            
            for (let i = 1; i <= 30; i++) {
                const selecoesSalvas = sessionStorage.getItem('selecoes_' + i);
                if (selecoesSalvas) {
                    const selecoes = JSON.parse(selecoesSalvas);
                    for (const name in selecoes) {
                        let value = Number(selecoes[name]);
                        // data['exatas'] += value*exatas;
                        // data['biologicas'] += value*biologicas;
                        // data['engenharias'] += value*engenharias;
                        // data['saude'] += value*saude;
                        // data['agrarias'] += value*agrarias;
                        // data['linguistica'] += value*linguistica;
                        // data['sociais'] += value*sociais;
                        // data['humanas'] += value*humanas;
                        //var perguntas = JSON.parse(perguntasData);

                        console.log(value);
                    }
                }
            }
            console.log(data);

            xhr.send(JSON.stringify(data));
            xhr.onload = function () {
                if (xhr.status === 200) {
                    // Redirecione para a página de perfil ou outra página de destino
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
