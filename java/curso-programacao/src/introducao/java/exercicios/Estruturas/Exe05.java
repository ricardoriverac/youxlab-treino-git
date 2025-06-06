package introducao.java.exercicios.Estruturas;

import java.util.Locale;
import java.util.Scanner;

public class Exe05 {
    /// Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A
    /// seguir, calcule e mostre o valor da conta a pagar.
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int codigo , qnt;
        double valor;
        codigo = sc.nextInt();
        qnt = sc.nextInt();

        switch (codigo) {
            case 1:
                valor = 4 * qnt;
                System.out.printf("Total %.2f", valor);
                break;
            case 2:
                valor = 4.50  * qnt;
                System.out.printf("Total %.2f", valor);

                break;
            case 3:
                valor = 5.00 * qnt;
                System.out.printf("Total %.2f", valor);
                break;
            case 4:
                valor = 2.00 * qnt;
                System.out.printf("Total %.2f", valor);
                break;
            case 5:
                valor = 13.50 * qnt;
                System.out.printf("Total %.2f", valor);
                break;
        }
    }
}
