package apllication;

import entities.Product;

import java.util.Locale;
import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc =new Scanner(System.in);

        Product product = new Product();
        System.out.println("Enter product data: ");
        System.out.println("Name: ");
        product.name = sc.nextLine();

        System.out.print("Price ");
        product.price = sc.nextDouble();

        System.out.println("Quantity in stock: ");
        product.quantity = sc.nextInt();

        System.out.println("Product data:"+product);
        System.out.println("Entre com os números de produtos a serem" +
                " adicionados no estoque");

        int quantity = sc.nextInt();
        product.addProducts(quantity);
        System.out.println("Updated data:"+product);

        System.out.println("Entre com o número de produtos para" +
                " serem removidos");
        quantity = sc.nextInt();
        product.removeProducts(quantity);

        System.out.println();
        System.out.println("Updated data: " + product);

        sc.close();

    }
}
