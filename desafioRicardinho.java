// model é usada para representar usuario em uma aplicação
// usada para armazenar e manipular dados de um usuario

import java.util.List;
import java.util.ArrayList;

class Pessoa{
    String nome;
    int idade;
    String cidade;

    public Pessoa(String nome, int idade, String cidade) {
        this.nome = nome;
        this.idade = idade;
        this.cidade = cidade;
    
    }
    @Override
    public String toString(){
        return "{" + nome + " " + idade + ", " + cidade + "}";
    }
}       

public class desafioRicardinho{
    public static void main(String[] args) {
        List<Pessoa> novasPessoas = new ArrayList();
        novasPessoas.add(new Pessoa("João,", 23, "Florianópolis"));
        System.out.println(novasPessoas);

    }
}