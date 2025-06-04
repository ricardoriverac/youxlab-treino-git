const nome = document.getElementById('inputNome')
const numero = document.getElementById('inputNumeroTelefone')
const cpf = document.getElementById('inputCpf')
const email = document.getElementById('inputEmail')

let arrayNome = []
let arrayNumero = []
let arrayCpf = []
let arrayEmail = []

const inserirLinha = (linha)=>{
    const valorInputNome = (nome.value)
    arrayNome.push(valorInputNome)
    console.log(arrayNome)

    const valorInputNumero = Number(numero.value)
    arrayNumero.push(valorInputNumero)
    console.log(arrayNumero)

    const valorInputCpf = Number(cpf.value)
    arrayCpf.push(valorInputCpf)
    console.log(arrayCpf)

    const valorInputEmail = (email.value)
    arrayEmail.push(valorInputEmail)
    console.log(arrayEmail)

    const novaLinha = document.createElement('tr')
    novaLinha.setAttribute('nome', arrayNome)
    novaLinha.setAttribute('numero', arrayNumero)
    novaLinha.setAttribute('cpf', arrayCpf)
    novaLinha.setAttribute('email', arrayEmail)
    novaLinha.innerHTML= linha
    
    console.log(novaLinha)
    return novaLinha
    
}
// const tabela = document.querySelector('#tabela')

// const novaLinha = document.createElement('tr')
// tabela.appendChild(novaLinha)