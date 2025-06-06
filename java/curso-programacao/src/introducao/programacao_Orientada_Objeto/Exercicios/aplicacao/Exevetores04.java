package introducao.programacao_Orientada_Objeto.Exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores04 {
    /// <h4 style= color:purple> Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
    /// tela todos os números pares, e também a quantidade de números pares. <h4/>
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        System.out.print("Quantos números você vai digitar: ");
        int quant = input.nextInt();
        int[] array = new int[quant];
        for (int i = 0; i < array.length; i++) {
            System.out.print("Digite um número: ");
            array[i] = input.nextInt();
        }
        System.out.println("Números pares: ");
        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 == 0) {
                System.out.print(array[i]);
            }
        }
    }
}
