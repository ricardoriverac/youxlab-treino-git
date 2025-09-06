package exercicios_Vetor;

import java.util.Locale;
import java.util.Scanner;

public class exercicio02 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        double[] vect = new double[n];

        for (int i = 0; i < n; i++) {
            vect[i] = sc.nextInt();
        }

        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += vect[i];
        }

        System.out.println(sum);

        sc.close();

    }
}