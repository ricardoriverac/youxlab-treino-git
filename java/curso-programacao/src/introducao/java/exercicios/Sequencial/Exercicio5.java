package introducao.java.exercicios.Sequencial;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio5 {
    /// Fazer um programa para ler o código de uma peça 1,
    /// o número de peças 1, o valor unitário de cada peça 1, o
    /// código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Calcule e mostre o valor a ser pago.
    public static void main(String[] args) {	Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int codigo1 , codigo2;
        int quantida1, quantida2;
        double preco1, preco2, total;

        codigo1 = sc.nextInt();
        quantida1 = sc.nextInt();
        preco1 = sc.nextDouble();

        codigo2 = sc.nextInt();
        quantida2 = sc.nextInt();
        preco2 = sc.nextDouble();

        total = preco1 * quantida1 + preco2 * quantida2;

        System.out.printf("valor total a pagar: R$ %.2f%n", total);

        sc.close();

    }

}
