package entidade;

public class Pessoa {
    private String nome;
    private char genero;

    public Pessoa(String nome, char genero) {
        this.nome = nome;
        this.genero = genero;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public char getGenero() {
        return genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }
    public String toString() {
        return "Nome: " + nome + ", Gênero: " + genero;
    }
}
