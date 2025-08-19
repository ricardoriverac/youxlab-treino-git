package Entidades;

// Pergaminho.java
public class Pergaminho extends Ferramentas {
    private String conteudo;

    public Pergaminho(String nome, String conteudo) {
        super(nome);
        this.conteudo = conteudo;
    }

    public String getConteudo() {
        return conteudo;
    }
}
