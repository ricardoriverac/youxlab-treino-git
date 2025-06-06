package introducao.java.exercicios.Sequencial;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double valor, area, pi = 3.14159;

        valor = sc.nextDouble();

        area = pi * valor * valor;

        System.out.printf("Area: %.4f%n", area);

        sc.close();



    }
}
