const caixasCursos=document.querySelector("#caixaCursos")
const botao_curso=[...document.querySelectorAll(".curso")]
const curso1_2=document.querySelector('#curso1_2')
const cursos = []
const boaoCursoSelecionado=document.getElementById('botaoCursoSelecionado')

const botaoAdicionarNovoCurso = document.getElementById('botaoAdicionarNovoCurso')

console.log(botaoAdicionarNovoCurso)

const carregarLista = () => {
    cursos.map((elemento,chave)=>{
        const novoElemento=document.createElement('div')
        novoElemento.setAttribute('id','c'+chave)
        novoElemento.setAttribute('class','curso c1')
        novoElemento.innerHTML=elemento

        const comandos=document.createElement('div')
        comandos.setAttribute('class','comandos')

        const rb=document.createElement('input')
        rb.setAttribute('type','radio')
        rb.setAttribute('name','rb_curso')

        comandos.appendChild(rb)

        caixasCursos.appendChild(novoElemento)
    })
}

carregarLista();


botaoAdicionarNovoCurso.addEventListener('click',(e) => { //Para cada vez que o botão for clicado
    const input = document.getElementById("nomeCurso") // adiciona o elemento com a div "nomeCurso" na var input
    elemento = input.value  // adiciona na var o input com seu valor na var elemento

    cursos.push(elemento) // coloquei o elemento no array
    carregarLista()  // adiciona a função
    cursos.splice(0,1) //tira elemento da array
})