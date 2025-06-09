package java_introdução.curso_programacao;

import java.util.Locale;
import java.util.Scanner;

public class ex3_for {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        int x = input.nextInt();

        for (int i = 0; i < x; i ++){
            double a = input.nextDouble();
            double b = input.nextDouble();
            double c = input.nextDouble();

            double media = (a * 2.0 + b * 3.0 + c * 5.0) / 10.0;

            System.out.printf("%.1f%n", media);
        }

        input.close();
    }
}
