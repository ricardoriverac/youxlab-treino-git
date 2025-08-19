package entidades;

import java.util.ArrayList;
import java.util.List;

public class Produto {
    private String nome;
    protected Double preco;

    public Produto(){
    }

    public Produto(String nome, Double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Double getPreco() {
        return preco;
    }

    public void setPreco(Double preco) {
        this.preco = preco;
    }



    public String entiqueta() {

        String texto = nome + " - R$ " + String.format("%.2f", preco);
        return texto;
    }

}

