// EVENTO - addEventListener #P2

//AULA PRÁTICA:


//ADICIONANDO elementos em variáveis
const caixa1=document.querySelector('#caixa')  // elemento de id="caixa1"
const caixa2=document.querySelector('#caixa2')  // elemento de id="caixa2"
const botao=document.querySelector('#botao_copiar')  // elemento de id="botao_copiar"
const botao2=document.querySelector('#botao_voltar')
const todosCursos=[...document.querySelectorAll('.curso')]  // TODOS os elementos de class="curso"

//adiciona o EVENTO de click a TODOS os cursos
todosCursos.map((elementos)=>{
    elementos.addEventListener("click",(eventos)=>{
        const curso=eventos.target
        curso.classList.toggle("selecionado") // para cada elemento após o evento click a var curso recebe a class "selecionado"
        //significado de toggle()-->
    })
})

//ADICIONANDO as elementos SELECIONADOS na caixa 2
botao.addEventListener("click",()=>{
    const cursosSelecionados=[...document.querySelectorAll("#caixa > .selecionado")]
    cursosSelecionados.map((elemento)=>{
        caixa2.appendChild(elemento)
    })
})

botao2.addEventListener("click",()=>{
    const selecionadosCaixa2=[...document.querySelectorAll("#caixa2 .selecionado")]
    selecionadosCaixa2.map((elemento)=>{
        caixa1.appendChild(elemento)
        elemento.classList.remove("selecionado")
    })
})