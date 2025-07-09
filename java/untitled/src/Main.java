import entities.Product;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public  class Main {
    public static void main(String[] args) {
        List<Product> products = new ArrayList<>();

        products.add(new Product("TV" , 1200.00));
        products.add(new Product("Computador" , 5000.00));
        products.add(new Product("HD" , 120.00));

        // expressão lambda que e uma função anônima
        products.sort( (o1 , o2) -> -o1.getPrice().compareTo(o2.getPrice()));

        for (Product product : products) {
            System.out.println(product);
        }

    }
}