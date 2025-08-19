package execucao;

import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        System.out.print("Me diga quantos números deseja: ");
        int numero = sc.nextInt();
        double[] vect = new double[numero];

        double maiorvalor = 0;
        int posicao = 0;
        for (int contador = 0; contador < numero; contador++) {
            System.out.print("Digite número: ");
            vect[contador] = sc.nextDouble();

            if (vect[contador] > maiorvalor) {
                maiorvalor = vect[contador];
            }

        }
        System.out.print("O maior número é: ");
        System.out.println(maiorvalor);

        int posicaoMaior = 0;
        for (int contador = 0; contador < numero; contador++) {
            if (vect[contador] == maiorvalor) {
                posicaoMaior = contador;
            }
        }
        System.out.println("E esse número está na posição: "+ posicaoMaior);

    }
}