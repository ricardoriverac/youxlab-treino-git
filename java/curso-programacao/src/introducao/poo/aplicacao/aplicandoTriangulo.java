package introducao.poo.aplicacao;

import introducao.poo.entities.Triangulo;

import java.util.Locale;
import java.util.Scanner;

public class aplicandoTriangulo {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Triangulo x , y;
        x = new Triangulo();
        y = new Triangulo();

        System.out.println("De os parâmetros para o triângulo X");
        x.a = sc.nextDouble();
        x.b = sc.nextDouble();
        x.c = sc.nextDouble();
        System.out.println("De os parâmetros para o triângulo Y");
        y.a = sc.nextDouble();
        y.b = sc.nextDouble();
        y.c = sc.nextDouble();
        double areaX = x.area();


        double areaY = y.area();

        System.out.printf("grande area de X %.4f %n", areaX);
        System.out.printf("grande area de Y %.4f %n ", areaY);
        if (areaX > areaY){
            System.out.println("O maior e o X");
        }
        else {
            System.out.println("O maior e o Y");
        }
        sc.close();
    }
}
