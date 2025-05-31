package desafiolivro;
// 5. Sistema de Biblioteca

// Crie as classes:

//     Livro (título, autor, ISBN, disponível)

//     Usuario (nome, ID, lista de livros emprestados)

//     Biblioteca (lista de livros, lista de usuários)

// Implemente:

//     Métodos para emprestar e devolver livros

//     Verificar se o livro está disponível

//     Limitar o número de livros por usuário

class Livro{
    String titulo;
    String autor;
    String ISBN;
    boolean disponivel;

    public Livro(String titulo, String autor, int ISBN, boolean disponivel){
        this.titulo = titulo;
        this.autor = autor;
        this.ISBN = ISBN;
        this.disponivel = disponivel;

    }

    @Override
    public String toString(){
        return titulo + autor + ISBN + disponivel;
    };


}