// MÉTODO getElementById-->neste comando você pode obter um elemento específico indicando o <id>

// SINTAXE--> document.getElementById('NOME DO ID')

const divCurso1=document.getElementById('curso1')
console.log(divCurso1)
console.log(divCurso1.id) // imprime o id deste elemento
console.log(divCurso1.innerHTML) // imprime o innerHTML deste elemento

divCurso1.innerHTML='Curso de Javascript' // mudou o valor da propriedade innerHTML para 'Curso de javasrcript'

divCurso1.innerHTML='html' // voltando ao valor original do innerHTML

//Podendo obter todos os elementos divs
const divCurso2=document.getElementById('curso2')
const divCurso3=document.getElementById('curso3')
const divCurso4=document.getElementById('curso4')
const divCurso5=document.getElementById('curso5')
const divCurso6=document.getElementById('curso6')


//Colocando esses elementos detro de uma ARRAY
const arryElementos=[divCurso1,divCurso2,divCurso3,divCurso4,divCurso5,divCurso6]
console.log(arryElementos)

//podemos mudar o innerHTML de todos percorrendo esse array
for(div of arryElementos){
    div.innerHTML='Curso de Javascript' //alterou o innerHTML para 'Curso de Javascript'
}

// map também pode operar todos os elementos deste array
arryElementos.map((elemento)=>{ //neste map pega somente os elementos do array
    elemento.innerHTML='Javascript'//alterou o innerHTML para 'Javascript'
})

//Desta maneira conseguimos pegar os elementos da tela(DOM), trazer para vriáveis dentro do programa e operar essa variáveis
