var pagina = document.currentScript.getAttribute('pg');

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
    for (let i = 5 * pagina - 4; i <= 5 * pagina; i++) {
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

document.addEventListener('DOMContentLoaded', () => {
    // Ouve eventos de clique nos botões da paginação
    const botoesPaginacao = document.querySelectorAll('.pagination a.page-link');
    botoesPaginacao.forEach((botao) => {
        botao.addEventListener('click', () => {
            salvarSelecoes();
        });
    });
});


// Carrega as seleções ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    carregarSelecoes();
});
