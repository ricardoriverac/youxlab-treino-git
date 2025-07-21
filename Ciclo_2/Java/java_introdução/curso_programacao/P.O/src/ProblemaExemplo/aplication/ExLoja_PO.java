package ProblemaExemplo.aplication;

import ProblemaExemplo.entities.ProductLoja;


import java.util.Locale;
import java.util.Scanner;

public class ExLoja_PO {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        ProductLoja product = new ProductLoja();

        System.out.println("Enter product data: ");
        System.out.print("Name: ");
        product.name = input.nextLine();
        System.out.print("Price: ");
        product.price = input.nextDouble();
        System.out.print("Quantity in stock: ");
        product.quantity = input.nextInt();

        System.out.println();
        System.out.println("Product data: " + product);

        System.out.println();
        System.out.print("Enter the number of products to be added in stock: ");
        int quantity = input.nextInt();
        product.addProducts(quantity);

        System.out.println();
        System.out.println("Update data: "+ product);


        System.out.println();
        System.out.print("Enter the number of products to be remove in stock: ");
        quantity = input.nextInt();
        product.removeProducts(quantity);

        System.out.println();
        System.out.println("Update data: "+ product);

        input.close();
    }
}
