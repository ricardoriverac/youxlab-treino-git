package execucao;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int numero = sc.nextInt();
        double[] vect = new double[numero];

        for (int contador = 0; contador < numero; contador++) {
            vect[contador] = sc.nextDouble();
        }
        double soma = 0;
        for (int contador = 0; contador < numero; contador++) {
            soma += vect[contador];
        }
        double media = soma/numero;
        System.out.println("A soma dos valores e: "+ soma);
        System.out.println("A média e de: "+ media);
        }

    }