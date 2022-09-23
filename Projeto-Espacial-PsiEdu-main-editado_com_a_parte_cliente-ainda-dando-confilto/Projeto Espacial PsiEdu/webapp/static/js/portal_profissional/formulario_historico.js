// Divisorias de opções caso o profissional queira adicionar de 1 ou 3 formações acadêmicas.
var opcao = document.getElementById('opcao');
var opcao1 = document.getElementById('opcao1');

// Variaveis dos botoes adicionar/deletar
var adicionar_campo = document.getElementById('adicionar_campo');
var remover_campo = document.getElementById('remover_campo');


// Divisoria 0
var hr_div = document.getElementById('hr_div');
var curso_div = document.getElementById('curso_div');
var instituicao_div = document.getElementById('instituicao_div');
var data_inicio_div = document.getElementById('data_inicio_div');
var data_termino_div = document.getElementById('data_termino_div');
var descricao_div = document.getElementById('descricao_div');


// Divisoria 1
var hr_div1 = document.getElementById('hr_div1');
var curso_div1 = document.getElementById('curso_div1');
var instituicao_div1 = document.getElementById('instituicao_div1');
var data_inicio_div1 = document.getElementById('data_inicio_div1');
var data_termino_div1 = document.getElementById('data_termino_div1');
var descricao_div1 = document.getElementById('descricao_div1');

// Função para adicionar caso opção seja 0
adicionar_campo.onclick = function(){
var input_tags = opcao.getElementsByTagName('input');
if(input_tags.length == 0) {

    console.log("adicionou a divisoria 0")
    var hr = document.createElement('hr');
    // Instituição
    var label_instituicao = document.createElement('label');
    label_instituicao.setAttribute('for', 'nome_instituicao')
    label_instituicao.innerHTML = "Nome da Instituição";

    var nome_instituicao = document.createElement('input');
    nome_instituicao.setAttribute('id', 'nome_instituicao')
    nome_instituicao.setAttribute('name','nome_instituicao');
    nome_instituicao.setAttribute('class','form-control mt-5');
    nome_instituicao.setAttribute('type', 'text')

    // Curso
    var label_curso = document.createElement('label');
    label_curso.setAttribute('for', 'curso_academico')
    label_curso.innerHTML = "Nome do Curso";

    var curso_profissional = document.createElement('input');
    curso_profissional.setAttribute('id', 'curso_academico')
    curso_profissional.setAttribute('name','curso_academico');
    curso_profissional.setAttribute('class','form-control');
    curso_profissional.setAttribute('type', 'text')

    // Data inicio
    var label_data_inicio = document.createElement('label');
    label_data_inicio.setAttribute('for', 'data_inicio')
    label_data_inicio.innerHTML = "Data Início";

    var data_inicio = document.createElement('input');
    data_inicio.setAttribute('id', 'data_inicio')
    data_inicio.setAttribute('name','data_inicio');
    data_inicio.setAttribute('class','form-control');
    data_inicio.setAttribute('type', 'text')
    data_inicio.setAttribute('maxlength', '4')
    data_inicio.setAttribute('onkeypress', 'if (!isNaN(String.fromCharCode(window.event.keyCode))) return true; else return false;')

    // Data termino
    var label_data_termino = document.createElement('label');
    label_data_termino.setAttribute('for', 'data_termino')
    label_data_termino.innerHTML = "Data Termino";

    var data_termino = document.createElement('input');
    data_termino.setAttribute('id', 'data_termino')
    data_termino.setAttribute('name','data_termino');
    data_termino.setAttribute('class','form-control');
    data_termino.setAttribute('type', 'text')
    data_termino.setAttribute('maxlength', '4')
    data_termino.setAttribute('onkeypress', 'if (!isNaN(String.fromCharCode(window.event.keyCode))) return true; else return false;')


    // Descrição
    var label_descricao = document.createElement('label');
    label_descricao.setAttribute('for', 'descricao_academica')
    label_descricao.innerHTML = "Descrição de atividades ou resultados";

    var descricao_academica = document.createElement('textarea');
    descricao_academica.setAttribute('id', 'descricao_academica')
    descricao_academica.setAttribute('name','descricao_academica');
    descricao_academica.setAttribute('class','form-control');
    descricao_academica.setAttribute('style','white-space: pre-line');
    descricao_academica.setAttribute('row','3');
    
    hr_div.appendChild(hr); 
    // Criar instituicao
    instituicao_div.appendChild(label_instituicao); 
    instituicao_div.appendChild(nome_instituicao); 

    // Criar curso
    curso_div.appendChild(label_curso); 
    curso_div.appendChild(curso_profissional);

    // Criar data inicio
    data_inicio_div.appendChild(label_data_inicio); 
    data_inicio_div.appendChild(data_inicio);

    // Criar data termino
    data_termino_div.appendChild(label_data_termino); 
    data_termino_div.appendChild(data_termino);

    // Criar descrição
    descricao_div.appendChild(label_descricao); 
    descricao_div.appendChild(descricao_academica);
 
}
else{ 
    // Função para adicionar caso opção seja 1
    var input_tags1 = opcao1.getElementsByTagName('input');
    if(input_tags1.length == 0) {
        console.log("adicionou a divisoria 1")
        var hr1 = document.createElement('hr');
        // Instituição
        var label_instituicao = document.createElement('label');
        label_instituicao.setAttribute('for', 'nome_instituicao')
        label_instituicao.innerHTML = "Nome da Instituição";
    
        var nome_instituicao = document.createElement('input');
        nome_instituicao.setAttribute('id', 'nome_instituicao')
        nome_instituicao.setAttribute('name','nome_instituicao');
        nome_instituicao.setAttribute('class','form-control mt-5');
        nome_instituicao.setAttribute('type', 'text')
    
        // Curso
        var label_curso = document.createElement('label');
        label_curso.setAttribute('for', 'curso_academico')
        label_curso.innerHTML = "Nome do Curso";
    
        var curso_profissional = document.createElement('input');
        curso_profissional.setAttribute('id', 'curso_academico')
        curso_profissional.setAttribute('name','curso_academico');
        curso_profissional.setAttribute('class','form-control');
        curso_profissional.setAttribute('type', 'text')
    
        // Data inicio
        var label_data_inicio = document.createElement('label');
        label_data_inicio.setAttribute('for', 'data_inicio')
        label_data_inicio.innerHTML = "Data Início";
    
        var data_inicio = document.createElement('input');
        data_inicio.setAttribute('id', 'data_inicio')
        data_inicio.setAttribute('name','data_inicio');
        data_inicio.setAttribute('class','form-control');
        data_inicio.setAttribute('type', 'text')
        data_inicio.setAttribute('maxlength', '4')
        data_inicio.setAttribute('onkeypress', 'if (!isNaN(String.fromCharCode(window.event.keyCode))) return true; else return false;')

        // Data termino
        var label_data_termino = document.createElement('label');
        label_data_termino.setAttribute('for', 'data_termino')
        label_data_termino.innerHTML = "Data Termino";
    
        var data_termino = document.createElement('input');
        data_termino.setAttribute('id', 'data_termino')
        data_termino.setAttribute('name','data_termino');
        data_termino.setAttribute('class','form-control');
        data_termino.setAttribute('type', 'text')
        data_termino.setAttribute('maxlength', '4')
        data_termino.setAttribute('onkeypress', 'if (!isNaN(String.fromCharCode(window.event.keyCode))) return true; else return false;')
    
    
        // Descrição
        var label_descricao = document.createElement('label');
        label_descricao.setAttribute('for', 'descricao_academica')
        label_descricao.innerHTML = "Descrição de atividades ou resultados";
    
        var descricao_academica = document.createElement('textarea');
        descricao_academica.setAttribute('id', 'descricao_academica')
        descricao_academica.setAttribute('name','descricao_academica');
        descricao_academica.setAttribute('class','form-control mb-5');
        descricao_academica.setAttribute('style','white-space: pre-line');
        descricao_academica.setAttribute('row','3');
        

        hr_div1.appendChild(hr1); 
        // Criar instituicao
        instituicao_div1.appendChild(label_instituicao); 
        instituicao_div1.appendChild(nome_instituicao); 
    
        // Criar curso
        curso_div1.appendChild(label_curso); 
        curso_div1.appendChild(curso_profissional);
    
        // Criar data inicio
        data_inicio_div1.appendChild(label_data_inicio); 
        data_inicio_div1.appendChild(data_inicio);
    
        // Criar data termino
        data_termino_div1.appendChild(label_data_termino); 
        data_termino_div1.appendChild(data_termino);
    
        // Criar descrição
        descricao_div1.appendChild(label_descricao); 
        descricao_div1.appendChild(descricao_academica);
    }
}
    // Se existir a divisoria 1, desabilite o botão para adicionar mais campos.
    if(input_tags1) {
        adicionar_campo.setAttribute('class', 'btn btn-info btn-sm disabled')
    }

    remover_campo.setAttribute('class', 'btn btn-danger btn-sm') 
}

remover_campo.onclick = function(){

    var hr_tag = hr_div.getElementsByTagName('hr');
    var label_instituticao_tag = instituicao_div.getElementsByTagName('label');
    var instituicao_tag = instituicao_div.getElementsByTagName('input');
    var label_curso_tag = curso_div.getElementsByTagName('label');
    var curso_tag = curso_div.getElementsByTagName('input');
    var label_data_inicio_tag = data_inicio_div.getElementsByTagName('label');
    var data_inicio_tag = data_inicio_div.getElementsByTagName('input');
    var label_data_termino_tag = data_termino_div.getElementsByTagName('label');
    var data_termino_tag = data_termino_div.getElementsByTagName('input');
    var label_descricao_tag = descricao_div.getElementsByTagName('label');
    var descricao_tag = descricao_div.getElementsByTagName('textarea');


    var hr_tag1 = hr_div1.getElementsByTagName('hr');
    var label_instituticao_tag1 = instituicao_div1.getElementsByTagName('label');
    var instituicao_tag1 = instituicao_div1.getElementsByTagName('input');
    var label_curso_tag1 = curso_div1.getElementsByTagName('label');
    var curso_tag1 = curso_div1.getElementsByTagName('input');
    var label_data_inicio_tag1 = data_inicio_div1.getElementsByTagName('label');
    var data_inicio_tag1 = data_inicio_div1.getElementsByTagName('input');
    var label_data_termino_tag1 = data_termino_div1.getElementsByTagName('label');
    var data_termino_tag1 = data_termino_div1.getElementsByTagName('input');
    var label_descricao_tag1 = descricao_div1.getElementsByTagName('label');
    var descricao_tag1 = descricao_div1.getElementsByTagName('textarea');

    if(hr_tag1 && instituicao_tag1.length && curso_tag1.length && data_inicio_tag1.length && data_termino_tag1.length && descricao_tag1.length && label_instituticao_tag1.length && label_curso_tag1.length && label_data_inicio_tag1.length && label_data_termino_tag1.length && label_descricao_tag1.length) {

        console.log("removou a divisoria 1")

        hr_div1.removeChild(hr_tag1[(hr_tag1.length) - 1]);

        
        instituicao_div1.removeChild(label_instituticao_tag1[(label_instituticao_tag1.length) - 1]);
        instituicao_div1.removeChild(instituicao_tag1[(instituicao_tag1.length) - 1]);

        curso_div1.removeChild(label_curso_tag1[(label_curso_tag1.length) - 1]);
        curso_div1.removeChild(curso_tag1[(curso_tag1.length) - 1]);

        data_inicio_div1.removeChild(label_data_inicio_tag1[(label_data_inicio_tag1.length) - 1]);
        data_inicio_div1.removeChild(data_inicio_tag1[(data_inicio_tag1.length) - 1]);

        data_termino_div1.removeChild(label_data_termino_tag1[(label_data_termino_tag1.length) - 1]);
        data_termino_div1.removeChild(data_termino_tag1[(data_termino_tag1.length) - 1]);

        descricao_div1.removeChild(label_descricao_tag1[(label_descricao_tag1.length) - 1]);
        descricao_div1.removeChild(descricao_tag1[(descricao_tag1.length) - 1]);
    }
    else
    {
        console.log("removou a divisoria 0")

        hr_div.removeChild(hr_tag[(hr_tag.length) - 1]);

        instituicao_div.removeChild(label_instituticao_tag[(label_instituticao_tag.length) - 1]);
        instituicao_div.removeChild(instituicao_tag[(instituicao_tag.length) - 1]);

        curso_div.removeChild(label_curso_tag[(label_curso_tag.length) - 1]);
        curso_div.removeChild(curso_tag[(curso_tag.length) - 1]);

        data_inicio_div.removeChild(label_data_inicio_tag[(label_data_inicio_tag.length) - 1]);
        data_inicio_div.removeChild(data_inicio_tag[(data_inicio_tag.length) - 1]);

        data_termino_div.removeChild(label_data_termino_tag[(label_data_termino_tag.length) - 1]);
        data_termino_div.removeChild(data_termino_tag[(data_termino_tag.length) - 1]);

        descricao_div.removeChild(label_descricao_tag[(label_descricao_tag.length) - 1]);
        descricao_div.removeChild(descricao_tag[(descricao_tag.length) - 1]);

        remover_campo.setAttribute('class', 'btn btn-danger btn-sm disabled') 
    }

    adicionar_campo.setAttribute('class', 'btn btn-info btn-sm') 
}



// Função para o template do formulário grátis criado por @bbbootstrap62244

const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".step-forms");
const progressSteps = document.querySelectorAll(".progress-step");


let formStepsNum = 0;

nextBtns.forEach((btn) => {
        btn.addEventListener("click", () => {
            formStepsNum++;
            updateFormSteps();
            updateProgressbar();
    });
});

prevBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
        formStepsNum--;
        updateFormSteps();
        updateProgressbar();
    });
});

function updateFormSteps() {
    formSteps.forEach((formStep) => {
        
        formStep.classList.contains("step-forms-active") &&
        formStep.classList.remove("step-forms-active");
});

formSteps[formStepsNum].classList.add("step-forms-active");
}

function updateProgressbar() {
    progressSteps.forEach((progressStep, idx) => {
        if (idx < formStepsNum + 1) {

        progressStep.classList.add("progress-step-active");

        } else {

        progressStep.classList.remove("progress-step-active");

        }
    });

    progressSteps.forEach((progressStep, idx) => {
        if (idx < formStepsNum) {

        progressStep.classList.add("progress-step-check");
        } else {

        progressStep.classList.remove("progress-step-check");
        }
    });

    const progressActive = document.querySelectorAll(".progress-step-active");

    progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}