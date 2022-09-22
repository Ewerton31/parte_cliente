var opcao = document.getElementById('opcao');
var adicionar_campo = document.getElementById('adicionar_campo');
var remover_campo = document.getElementById('remover_campo');

adicionar_campo.onclick = function(){
var input_tags = opcao.getElementsByTagName('textarea');

if(input_tags.length == 0) {
    var novoCampo = document.createElement('textarea');
    novoCampo.setAttribute('style', 'white-space: pre-line')
    novoCampo.setAttribute('id', 'formacao_academica')
    novoCampo.setAttribute('name','formacao_academica');
    novoCampo.setAttribute('class','form-control mb-3');
    novoCampo.setAttribute('row','3');
    novoCampo.setAttribute('placeholder','Formação acadêmica1*');
    
    var novoCampo2 = document.createElement('textarea');
    novoCampo2.setAttribute('style', 'white-space: pre-line')
    novoCampo2.setAttribute('id', 'formacao_academica2')
    novoCampo2.setAttribute('name','formacao_academica2');
    novoCampo2.setAttribute('class','form-control mb-3');
    novoCampo2.setAttribute('row','3');
    novoCampo2.setAttribute('placeholder','Formação acadêmica2*');
    
    opcao.appendChild(novoCampo);
    opcao.appendChild(novoCampo2);  
}
else{
    var novoCampo2 = document.createElement('textarea');
    novoCampo2.setAttribute('style', 'white-space: pre-line')
    novoCampo2.setAttribute('id', 'formacao_academica2')
    novoCampo2.setAttribute('name','formacao_academica2');
    novoCampo2.setAttribute('class','form-control mb-3');
    novoCampo2.setAttribute('row','3');
    novoCampo2.setAttribute('placeholder','Formação acadêmica2*');

    opcao.appendChild(novoCampo2);  
}
    
    if(input_tags.length == 2) {
    adicionar_campo.setAttribute('class', 'btn btn-info btn-sm disabled')
    }
}

remover_campo.onclick = function(){
    var input_tags = opcao.getElementsByTagName('textarea');
    if(input_tags.length > 0) {
    opcao.removeChild(input_tags[(input_tags.length) - 1]);
    var adicionar_campo = document.getElementById('adicionar_campo');
    adicionar_campo.setAttribute('class', 'btn btn-info btn-sm')  
    }
}


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


document.getElementById("submit-form").addEventListener("click", function () {

progressSteps.forEach((progressStep, idx) => {
if (idx <= formStepsNum) {

progressStep.classList.add("progress-step-check");
} else {

progressStep.classList.remove("progress-step-check");
}
});

var forms = document.getElementById("forms");
forms.classList.remove("form");
forms.innerHTML = '<div class="welcome"><div class="content"><svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none"/><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/></svg><h2>Thanks for signup!</h2><span>We will contact you soon!</span><div></div>';
});