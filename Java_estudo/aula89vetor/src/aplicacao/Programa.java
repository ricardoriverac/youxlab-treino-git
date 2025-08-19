package aplicacao;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        double[] vect = new double [n];

        for (int contador =0; contador<n; contador++  ){
            vect[contador] = sc.nextDouble();

        }

        double soma = 0;
        for (int contador = 0; contador<n; contador++ ){
            soma += vect[contador];
        }

        double media = soma /n;

        System.out.println("A media desse vetor e: " + media);

        sc.close();
    }
}
