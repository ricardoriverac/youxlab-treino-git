package introducao.java.exercicios.Estruturas;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio02 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double a , b , c;
        System.out.print("A: ");
        a = sc.nextDouble();
        System.out.print("B: ");
        b = sc.nextDouble();
        System.out.print("C: ");
        c = sc.nextDouble();

        double delta = b * b  - 4.0 * a * c;
        if (a == 0 || delta < 0.0){
            System.out.println("Impossivel calcular");
        }
        else {
            double r1 = (-b + Math.sqrt(delta)) / (2.0 * a);
            double r2 = (-b - Math.sqrt(delta)) / (2.0 * a);
            System.out.printf("R1 = %.5f %n" , r1);
            System.out.printf("R2 = %.5f" , r2);
        }

        sc.close();
    }
}
