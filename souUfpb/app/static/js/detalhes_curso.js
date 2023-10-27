var nome = document.currentScript.getAttribute('nome');
var text = nome.split('-');
var nomeCurso = document.getElementById("nomeCurso");
var linhas = [];

for (let i=0;i<text.length;i++) 
    text[i] = text[i].trim();

switch (text[3]){
    case 'M':
        text[3] = 'Manhã';
        break;
    case 'T':
        text[3] = 'Tarde';
        break;
    case 'N':
        text[3] = 'Noite';
        break;
    case 'MT':
        text[3] = 'Manhã/Tarde';
        break;
    default:
}

text[1] = "Local: " + text[1];
text[2] = "Modalidade: " + text[2];
text[3] = "Turno: " + text[3];
text[4] = "Grau acadêmico: " + text[4];

for (let i=1;i<text.length;i++){
    var linha = document.createElement("p");
    linha.textContent = text[i];
    linhas.push(linha);
}

var linha0 = document.createElement("p");
linha0.textContent = text[0];
linha0.style = "font-weight: bold; font-size: 28px; margin-bottom: 4vh; color: #3b99c1";
nomeCurso.appendChild(linha0);

var info = document.getElementById("info");
for (let i=linhas.length-1;i>=0; i--) {
    linhas[i].style = "margin-bottom: 0; margin-top: 0; margin-left: 2vw; font-size: 22px";
    info.prepend(linhas[i]);
}

var curso = document.getElementById("nomeCurso").getAttribute('curso-pk');

fetch(`/get_data/?id=${curso}`)
.then(response => response.json())
.then(data => {
    var listaPeriodos = document.getElementById("periodos");
    var dropdown = document.getElementsByClassName('dropdown-content')[0];
    var periodos = data['dados'];
    for (let i=0;i<periodos.length;i++) {
        if (periodos[i].length == 0) continue;
        var opcao = document.createElement("a");
        opcao.textContent = i + "º período";
        opcao.setAttribute('href', '#'+i);
        
        opcao.addEventListener('click', function(event) {
            event.preventDefault();
            const targetElement = document.getElementById(i);
            
            if (targetElement) {
                const offset = 100;
                const targetOffset = targetElement.offsetTop - offset;
                window.scrollTo({ top: targetOffset, behavior: 'smooth' });
            }
        });
        dropdown.appendChild(opcao);

        var periodo = document.createElement("div");
        periodo.id = i;
        periodo.style = "border-style: solid; border-radius: 30px; border-color: #3b99c1; margin-bottom: 2vh; padding-bottom: 4vh";
        listaPeriodos.appendChild(periodo);

        var title = document.createElement("p");
        title.textContent = i + "º período";
        title.style = "color: #3b99c1; font-size: 28px; font-weight: bold; margin: 2vh 0 4vh 2vw";
        periodo.appendChild(title);

        for (let j = 0; j<periodos[i].length; j++) {
            var disciplina = document.createElement("p");
            disciplina.textContent = periodos[i][j];
            disciplina.style = "margin-left: 4vw;";
            periodo.appendChild(disciplina);
        }
    }
})
.catch(error => {
    console.error(error);
});