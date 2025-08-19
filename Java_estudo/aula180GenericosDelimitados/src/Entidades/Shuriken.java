package Entidades;

// Shuriken.java
public class Shuriken extends Ferramentas {
    private int tamanho;

    public Shuriken(String nome, int tamanho) {
        super(nome);
        this.tamanho = tamanho;
    }

    public int getTamanho() {
        return tamanho;
    }
}

