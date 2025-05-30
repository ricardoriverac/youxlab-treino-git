function alunos(aluno, nota){
    this.aluno = aluno
    this.nota = nota
    console.log(aluno)
    console.log(nota)
    this.dados_arrow = function(){
        setTimeout(()=>{
            console.log(this.aluno)
            console.log(this.nota)
        },2000)
    }
}

const al1 = new alunos("ana", 100)
al1.dados_arrow()