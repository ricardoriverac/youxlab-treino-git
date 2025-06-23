package introducao.poo.composition.exercicios.entities;

public class OrdemItem {
    private Integer quantity;
    private Double price;

    private Product product;

    public OrdemItem() {
    }

    public OrdemItem(Integer quantity, Double price , Product product) {
        this.quantity = quantity;
        this.price = price;
        this.product = product;
    }

    public Integer getQuantity() {
        return quantity;
    }

    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
    }

    public Double getPrice() {
        return price;
    }

    public Product getProduct() {
        return product;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public Double subtotal(){
        return price * quantity;
    }

    @Override
    public String toString() {
        return getProduct().getName()
                + ", $"
                + String.format("%.2f" , price)
                + ", quantity: "
                + quantity
                + ", Subtotal: $"
                + String.format("%.2f" , subtotal());
    }

}
