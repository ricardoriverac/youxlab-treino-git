package introducao.poo.files.exercicies;

public class Product {
    private String nome;
    private double price;
    private int qnt;

    public Product() {
    }

    public Product(String nome, double price, int qnt) {
        this.nome = nome;
        this.price = price;
        this.qnt = qnt;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getQnt() {
        return qnt;
    }

    public void setQnt(int qnt) {
        this.qnt = qnt;
    }
}
