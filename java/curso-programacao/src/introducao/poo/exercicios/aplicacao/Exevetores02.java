package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores02 {
    /// Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
    /// - Imprimir todos os elementos do vetor
    /// - Mostrar na tela a soma e a média dos elementos do vetor
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Quantos números você vai digitar: ");
        int n = input.nextInt();
        double[] array = new double[n];
        double soma = 0.0;
        for (int i = 0; i < array.length; i++) {
            System.out.print("Digite um número: ");
            array[i] = input.nextDouble();
            soma += array[i];
        }
        System.out.print("Valores: ");
        for (double num: array) {
            System.out.print(" " + num);
        }
        System.out.println();
        System.out.println("Soma:  " + soma);
        double avg = soma / array.length;
        System.out.println("Media: "+avg);
        input.close();
    }
}
