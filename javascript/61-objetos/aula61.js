const Pessoa={
    nome,
    idade,
    getNome:function(){
        return this.nome
    },
    getIdade:function(){
        return this.idade
    },
    setNome:function(nome){
        this.nome=nome
    },
    setIdade:function(idade){
        this.nome=idade
    }
}

const p2=Pessoa
const p3=Pessoa

p3.nome="Nagi"
p2["nome"]="Isagi"
Pessoa.setNome("Bachira")

console.log(Pessoa.nome)
console.log(p2.getNome())
console.log(p3.nome)
