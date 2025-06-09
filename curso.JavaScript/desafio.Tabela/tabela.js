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

    const botaoEditar = document.createElement('button')
    botaoEditar.textContent = 'Editar'
    botaoEditar.setAttribute('id', 'btnEditar')
    botaoEditar.setAttribute('class', 'btnEditar')

    botaoRemover.addEventListener('click', (evt)=>{
        novaLinha.remove()
    })
    botaoEditar.addEventListener('click', (evt)=>{
        const nome = novaLinha.cells[0].innerHTML
        const numero = novaLinha.cells[1].innerHTML
        const cpf = novaLinha.cells[2].innerHTML
        const email = novaLinha.cells[3].innerHTML
        const valores = [nome, numero, cpf, email]
        respostas.forEach((elemento, index) => {
            elemento.value = valores[index]
        })
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
    novaCedula.appendChild(botaoEditar)
    novaCedula.setAttribute('class', 'novacedula')
})
