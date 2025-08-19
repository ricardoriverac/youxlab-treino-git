package execucao;

import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        int numero = sc.nextInt();
        double[] vect = new double[numero];

        for (int contador= 0;contador<numero;contador++){
            vect[contador] = sc.nextDouble();
        }
        double soma = 0;
        for (int contador =0;contador<numero;contador++){
            soma += vect[contador];
        }
        System.out.println(soma);
        double media = soma/numero;

        System.out.println(media);
        for (int contador =0;contador<numero;contador++){
            System.out.println(vect[contador]);
        }
    }
}
