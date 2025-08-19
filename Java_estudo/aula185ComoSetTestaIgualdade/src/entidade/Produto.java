package entidade;

import java.util.Objects;

public class Produto implements Comparable<Produto> {
    private String name;
    private Double price;

    public Produto(String name, Double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Produto produto = (Produto) o;
        return Objects.equals(name, produto.name) && Objects.equals(price, produto.price);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, price);
    }
    @Override
    public int compareTo(Produto other){
        return name.toUpperCase().compareTo(other.getName().toUpperCase());


    }

    @Override
    public String toString() {
        return "Produto{" +
                "name='" + name + '\'' +
                ", price=" + price +
                '}';
    }
}