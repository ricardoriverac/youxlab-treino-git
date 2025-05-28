function aluno(nome, nota){
    this.nome = nome // Uma variável "nome" que recebe o valor do parâmetro nome
    this.nota = nota // This sempre faz referência á própria função

    this.dado_anonimo = function(){
        setTimeout(function(){
            console.log(this.nome)
        })
    }

aluno("Bruno", 100)