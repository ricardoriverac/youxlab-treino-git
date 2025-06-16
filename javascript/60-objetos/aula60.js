function Pessoa(pnome,pidade){ // Para todos os métodos tem que utilizar o "this"
    this.nome=pnome,
    this.idade=pidade,

    this.getNome = function(){
        return this.nome
    },
    this.getidade = function(){
        return this.idade
    },
    this.setNome = function(nome){
        this.nome=nome
    },
    this.setidade = function(idade){
        this.idade=idade
    },
    this.info = function(){
        console.log(`Nome..: ${this.nome}`)
        console.log(`Idade.: ${this.idade}`)
        console.log("---------------------")
    }
}

let pessoas=[]

const btn_add=document.querySelector("#btn_add")
const res=document.querySelector(".res")
const btn_limpar = document.querySelector("#btn_limpar")

const addPessoa=()=>{
    res.innerHTML="" // Limpa o elemento antes de adicionar uma nova pessoa
    pessoas.map((p)=>{
        const div=document.createElement("div")
        div.setAttribute("class","pessoa")
        div.innerHTML=`Nome:${p.getNome()}<br/>Idade:${p.getidade()}`
        res.appendChild(div)
    })
}

btn_add.addEventListener("click",(evt)=>{
    const nome=document.querySelector("#f_nome")
    const idade=document.querySelector("#f_idade")
    const p=new Pessoa(nome.value,idade.value)
    pessoas.push(p)
    nome.value=""
    idade.value=""
    nome.focus()
    addPessoa()
})

btn_limpar.addEventListener("click", (evt) => {
        res.innerHTML=""
        pessoas.splice(0, pessoas.length) // Esvazia o array

})
