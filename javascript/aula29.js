function aluno(nome, nota){
    this.nome = nome // Uma variável "nome" que recebe o valor do parâmetro nome
    this.nota = nota // This sempre faz referência á própria função

    this.dado_anonimo = function(){ // O this não funciona
        setTimeout(function(){
            console.log(this.nome)
            console.log(this.nota)
        },2000)
    }

    this.dado_arrow = function(){ // O this funciona
        setTimeout(() => {
            console.log(this.nome)
            console.log(this.nota)
        })
    },2000
}
const al1 = new aluno("Bruno", 100)
al1.dado_anonimo() // Após 2 segundos → imprime undefined, undefined
al1.dado_arrow() // Após 2 segundos → imprime Bruno, 100