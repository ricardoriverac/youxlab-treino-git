package Seção13.Exercicio3.Application;

import Seção13.Exercicio3.Entitites.Product;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Locale.setDefault(Locale.getDefault());
        Product product = new Product();


        System.out.print("Enter the number of products: ");
        int loopFor = input.nextInt();

        for (int a = 0; a < loopFor; a++) {
            System.out.println("Product #" + (a + 1) + " data");
            System.out.print("Common, used or imported (c/u/i)? ");
            input.nextLine();
            String CUI = input.nextLine().toUpperCase();

            while (!CUI.equals("C") && !CUI.equals("U") && !CUI.equals("I")) {
                System.out.print("Invalid option\nTry again: ");
                CUI = input.nextLine().toUpperCase();
            }

            System.out.print("Name: ");
            product.nameP = input.nextLine();
            System.out.print("Price: ");
            product.priceP = input.nextDouble();

            if (CUI.equals("I")){
                System.out.print("Customs fee: ");
                double customI = input.nextDouble();
            } else if (CUI.equals("U")) {
                System.out.print("Manufacture Date (DD/MM/YYYY): ");
                int dateU = input.nextInt();
            }
        }
    }
}
