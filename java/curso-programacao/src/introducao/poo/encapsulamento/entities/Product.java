package introducao.poo.encapsulamento.entities;

public class Product {
        private String nome;
        private double preco;
        private int quantidade;


    public Product(String nome, double preco , int quantidade){
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public double totalValoremStock(){
        return preco * quantidade;
    }
        public void addprodutos(int quantidade){
        this.quantidade += quantidade;
    }
        public void removeprodutos(int quantidade){
        this.quantidade -= quantidade;
    }
        public String toString(){
        return nome
                + ", R$"
                + String.format("%.2f" , preco)
                + " , "
                + quantidade
                + " unidade , Total valor em estoque R$"
                + String.format("%.2f",totalValoremStock());
    }
}
