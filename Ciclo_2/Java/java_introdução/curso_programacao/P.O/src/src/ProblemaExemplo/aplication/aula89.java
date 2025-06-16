package java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.aplication;

import java.util.Locale;
import java.util.Scanner;

public class aula89 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        double[] vect = new double[n];

        for (int i=0; i<n; i++){
            vect[i] = input.nextDouble();
        }

        double sum = 0.0;
            for (int i=0; i<n; i++){
                sum += vect[i];
            }

            double avg = sum / n;

        System.out.printf("Deu isso aqui: %.2f", avg);

        input.close();

    }
}
