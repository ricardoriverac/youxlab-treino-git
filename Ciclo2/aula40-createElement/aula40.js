//creatElement--> cria um elemento HTML e anexa ele na página

const caixa1=document.querySelector('#caixa1')
const botao_c=[...document.querySelectorAll('.curso')]

const cursos=['HTML','CSS','Javascript','PHP','React','MySQL','ReactNative']

//ADICIONANDO ESSES CURSOS DINÂMICAMENTE:

cursos.map((curso)=>{
    const novoElemento=document.createElement('div')
    novoElemento.setAttribute("id","c"+chave)  //valor do atributo chave
    novoElemento.setAttribute("class","curso c1") 
    novoElemento.innerHTML=curso
    caixa1.appendChild(novoElemento)
})


const novoElemento=document.createElement('div') // CRIOU UMA DIV

//ADICIONANDO UM ATRIBUTO:
novoElemento.setAttribute("id","c7")  //neste caso um id="c7"
novoElemento.setAttribute("class","curso c1") //neste caso uma class="curso c1"
// ADICIONA UM TEXTO NA DIV
novoElemento.innerHTML="ReactNatives" 

//ANEXANDO esse novo elemento dentro da var caixa
caixa1.appendChild(novoElemento)