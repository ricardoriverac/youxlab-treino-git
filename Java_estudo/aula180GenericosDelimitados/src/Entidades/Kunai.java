package Entidades;

// Kunai.java
public class Kunai extends Ferramentas {
    private String habilidade;

    public Kunai(String nome, String habilidade) {
        super(nome);
        this.habilidade = habilidade;
    }

    public String getHabilidade() {
        return habilidade;
    }
}
