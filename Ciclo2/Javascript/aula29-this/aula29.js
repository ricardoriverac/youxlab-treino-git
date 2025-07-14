// OPERADOR THIS dentro de funções

function aluno(nome,nota){
    this.nome=nome //tipo uma var declarada para função que recebe o valor do parâmetro nome
    this.nota=nota

this.dados_anonimo=function(){ // setTimeout()-->gera um atraso na excução
        setTimeout(function(){ // NÃO FUNCIONA com function
            console.log(this.nome)
            console.log(this.nota)
        },1000)  
    }

    this.dados_arrow=function(){ // setTimeout()-->gera um atraso na excução
        setTimeout(()=>{ // FUNCIONA com arrow function
            console.log(this.nome)
            console.log(this.nota)
        },1000)  
    }
}

const alunos=new aluno('Sophia',25)
alunos.dados_anonimo()
alunos.dados_arrow()