package application.rectangle;

import java.util.Locale;
import java.util.Scanner;


public class RectanglePrincipal {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US); // Garante o uso de ponto decimal
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter rectangle width and height:");
        double w = sc.nextDouble();
        double h = sc.nextDouble();

        Rectangle rect = new Rectangle(w, h);
    }
}