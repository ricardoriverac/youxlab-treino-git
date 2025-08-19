package application;

import entities.Triangulo;

import java.util.Locale;
import java.util.Scanner;

public class AreaTriangulo {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Triangulo x,y;
        x = new Triangulo();
        y = new Triangulo();

        System.out.println("Entre com as medidas do triângulo X ");
        x.a = sc.nextDouble();
        x.b = sc.nextDouble();
        x.c = sc.nextDouble();

        System.out.println("Entre com as medidas do triângulo Y ");
        y.a = sc.nextDouble();
        y.b = sc.nextDouble();
        y.c = sc.nextDouble();

//        double p = (x.a + x.b + x.c) / 2;
//        double areaX = Math.sqrt(p * (p - x.a) * (p - x.b) * (p - x.c));
//
//        p = (y.a + y.b + y.c) / 2;
//        double areaY = Math.sqrt(p * (p - y.a) * (p - y.b) * (p - y.c));

        double areaX = x.area();
        double areaY = y.area();

        System.out.printf("Triângulo x area: %.4f%n ", areaX);
        System.out.printf("Triângulo y area: %.4f%n ", areaY);

        if (areaX > areaY) {
            System.out.println("Large area: X ");
        } else {System.out.println("Large area: Y ");
        }
        sc.close();

    }
}

