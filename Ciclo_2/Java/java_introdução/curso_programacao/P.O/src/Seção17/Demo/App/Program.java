package Seção17.Demo.App;


import Seção17.Demo.Ent.Product;

import java.util.HashSet;
import java.util.Set;

public class Program {
    public static void main(String[] args) {

        Set<Product> set = new HashSet<>();

        set.add(new Product("Tv", 900.0));
        set.add(new Product("Notbook", 1200.0));
        set.add(new Product("Tablet", 400.0));

        Product prod = new Product("Notbook", 1200.0);
        System.out.println(set.contains(prod));
    }
}
