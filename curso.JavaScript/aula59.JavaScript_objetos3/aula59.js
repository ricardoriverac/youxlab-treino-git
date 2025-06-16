class pessoa{
    constructor(pnome, pidade){
        this.nome = pnome
        this.idade = pidade
    }
    getNome(){
        return this.nome
    }
    getIdade(){
        return this.idade
    }
    setNome(nome){
        this.nome = nome
    }
    setIdade(idade){
        this.idade = idade
    }
    info(){
        console.log(`Nome: ${this.nome}`)
        console.log(`Idade: ${this.idade}`)
        console.log('----------------')
    }
} 

const btnAdicionar = document.querySelector('#btnAdicionar')
const infos = document.querySelector('#informaçoes')
const btnLimpar = document.querySelector('#btnLimpar')

let pessoas = []

const addPessoa=()=>{
    infos.innerHTML =''
    pessoas.map((p)=>{
        const div = document.createElement('div')
        div.setAttribute('id', 'informaçoes')
        div.innerHTML = `Nome: ${p.getNome()} </br> Idade: ${p.getIdade()}`
        infos.appendChild(div)
    })
}


btnAdicionar.addEventListener('click', (evt)=>{
    const nome = document.querySelector('#nome')
    const idade = document.querySelector('#idade')
    const p = new pessoa(nome.value, idade.value)
    pessoas.push(p)
    nome.value = ""
    idade.value = ""
    nome.focus()
    addPessoa()
})

btnLimpar.addEventListener('click', (evt)=>{
    infos.remove()
})