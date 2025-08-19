package publica;

import util.calculadora;

import java.util.Locale;
import java.util.Scanner;

public class Program {

    public static double PI = 3.14159;

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Entre com o raio: ");
        double raio = sc.nextDouble();

        double c = calculadora.circumference(raio);

        double v = calculadora.volume(raio);

        System.out.printf("Circumference: %.2f%n", c);
        System.out.printf("Volume: %.2f%n ", v);
        System.out.printf("pi value: %.2f%n", calculadora.PI);

        sc.close();

    }
}
////    }
////    public static double circumference(double raio){
////        return 2.0 * PI * raio;
////    }
////    public static double volume(double raio){
////        return 4.0 * PI * raio * raio * raio / 3.0;
////    }
//}
