package java_introdução.curso_programacao;

import java.util.Locale;
import java.util.Scanner;

public class ex4_for {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        for (int i = 0; i < n; i++) {

            int a = input.nextInt();
            int b = input.nextInt();

            if (b == 0) {
                System.out.println("Ta querendo demais já (Divisao impossivel)");
            }
            else {
                    double divisao = a / b;
                    System.out.printf("%.1f%n", divisao);
            }
        }
        input.close();
    }
}