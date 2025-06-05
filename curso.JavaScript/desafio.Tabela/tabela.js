const btnRemover = document.getElementsByClassName('btnRemover')
const btnInserir = document.getElementById('btnInserir')

const pessoas = [...document.querySelectorAll('.pessoa')]
const tabela = document.getElementById('estilo')
const respostas = document.querySelectorAll('#digite')

console.log(pessoas)
console.log(tabela)


btnInserir.addEventListener('click', (evt)=>{
    const novaLinha = tabela.insertRow(-1)
    const botaoRemover = document.createElement('button')
    botaoRemover.textContent = 'Remover'
    botaoRemover.setAttribute('id', 'btnRemover')
    botaoRemover.setAttribute('class', 'btnRemover')

    botaoRemover.addEventListener('click', (evt)=>{
        novaLinha.remove()
    })
    novaLinha.setAttribute('class','pessoa')
    for(elemento of respostas){
        var novaCedula = novaLinha.insertCell(-1)
        novaCedula.innerHTML=elemento.value
        elemento.value = ''
    }
    var novaCedula = novaLinha.insertCell(-1)
    novaCedula.appendChild(botaoRemover)
})