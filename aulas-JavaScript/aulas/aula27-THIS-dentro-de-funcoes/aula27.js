function aluno(nome, nota){
    this.nome = nome
    this.nota = nota

    this.dadosAnonimo = function(){
        setTimeout(function(){  // setTimeout é delay e ele sombreia o this
            console.log(this.nome)
            console.log(this.nota)
        },2000)
    }

    this.dadosArrow = function(){
        setTimeout(()=>{  // quando usa => ele não sombreia
            console.log(this.nome)
            console.log(this.nota)
        },2000)
    }
}

const aluno1 = new aluno('Tayla', 100)
aluno1.dadosAnonimo()
aluno1.dadosArrow()