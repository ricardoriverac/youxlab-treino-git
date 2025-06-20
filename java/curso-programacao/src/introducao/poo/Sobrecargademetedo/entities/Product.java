package introducao.poo.Sobrecargademetedo.entities;

public class Product {
    public String name;
    public double price;
    public int quantity;

    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
    // Sobre carga de mêtedo é quando um metêdo tem muitos ai posso fazer o mesmo método com menos parâmetros
    public Product(String name, double price) {
        this.name = name;
        this.price = price;

    }
}