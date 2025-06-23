package introducao.poo.entities;

public class Product {
    public String nome;
    public double preco;
    public int quantidade;

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
