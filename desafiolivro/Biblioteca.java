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

import java.util.List;
import java.util.ArrayList;


class Biblioteca {
    List<Usuario> Usuario;
    List<Livro> Livros;
    

    void estaDisponivel(){
        for(Usuario usuario : Usuario){
            String disponivel (String) Usuario.get('disponivel');
        }

    }
    


}