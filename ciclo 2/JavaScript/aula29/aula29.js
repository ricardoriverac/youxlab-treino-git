// função construtora chamada 'aluno' que recebe 'nome' e 'nota' como parâmetros
function aluno(nome, nota) {
    // atribui o valor do parâmetro 'nome' à propriedade 'nome' do objeto
    this.nome = nome;
    // atribui o valor do parâmetro 'nota' à propriedade 'nota' do objeto
    this.nota = nota;

    // método 'dados_anonimo' definido como uma função tradicional
    this.dados_anonimo = function() {
        // settimeout executa a função após 1000 milissegundos (1 segundo)
        setTimeout(function() {
            // dentro de uma função tradicional, 'this' não se refere ao objeto 'aluno'
            // portanto, 'this.nome' e 'this.nota' serão 'undefined' ou não terão os valores esperados
            console.log(this.nome);
            console.log(this.nota);
        }, 1000);
    };

    // método 'dados_arrow' definido como uma arrow function
    this.dados_arrow = function() {
        // settimeout executa a função após 1000 milissegundos (1 segundo)
        setTimeout(() => {
            // arrow functions não possuem seu próprio 'this'
            // elas herdam o 'this' do contexto onde foram definidas
            // portanto, 'this.nome' e 'this.nota' referem-se corretamente ao objeto 'aluno'
            console.log(this.nome);
            console.log(this.nota);
        }, 1000);
    };
}

// cria uma nova instância de 'aluno' com o nome 'lexi' e nota 25
const alunos = new aluno('lexi', 25);

// chama o método 'dados_anonimo' da instância 'alunos'
// devido ao uso de função tradicional, 'this' dentro de settimeout não se refere ao objeto 'aluno'
// resultado: 'undefined' será impresso no console
alunos.dados_anonimo();

// chama o método 'dados_arrow' da instância 'alunos'
// devido ao uso de arrow function, 'this' dentro de settimeout herda o contexto correto
// resultado: 'sophia' e '25' serão impressos no console após 1 segundo
alunos.dados_arrow();
