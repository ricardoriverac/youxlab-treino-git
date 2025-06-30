package Seção13.Exercicio3.Application;

import java.util.Locale;
import java.util.Scanner;

public class não {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Locale.setDefault(Locale.getDefault());

        System.out.print("Enter the number of products: ");
        int loopFor = input.nextInt();

        for (int a = 0; a < loopFor; a++) {
            System.out.println("Product #" + (a + 1) + " data");
            System.out.print("Common, used or imported (c/u/i)? ");

            String CUI = input.nextLine().toUpperCase();

            while (!CUI.equals("C") && !CUI.equals("U") && !CUI.equals("I")) {
                System.out.print("Invalid option\nTry again: ");
                CUI = input.nextLine().toUpperCase();
            }

            if (CUI == "I"){
                System.out.print("Name: ");
                String name = input.nextLine();
                System.out.print("Price: ");
                double price = input.nextDouble();
                System.out.print("Customs fee: ");
                double custom = input.nextDouble();
            } else if (CUI == "U") {
                System.out.print("Name: ");
                String name = input.nextLine();
                System.out.print("Price: ");
                double price = input.nextDouble();
                System.out.print("Manufacture Date (DD/MM/YYYY): ");
                int date = input.nextInt();
            } else {
                System.out.print("Name: ");
                String name = input.nextLine();
                System.out.print("Price: ");
                double price = input.nextDouble();
            }


        }







    }
}
