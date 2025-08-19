package aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int numero = sc.nextInt();
        double[] vect = new double[numero];
        double valoresNegativos = 0;

        for (int contador = 0; contador < numero; contador++) {
            vect[contador] = sc.nextDouble();

            if (vect[contador] < 0){
               // System.out.println(vect[contador]);
                valoresNegativos = vect[contador];
                System.out.println(valoresNegativos);
            }
        }

    }
}
