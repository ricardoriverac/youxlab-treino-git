package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores05 {
    /// <p style= color:purple>Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
    /// o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
    /// considerando a primeira posição como 0 (zero). <p/>
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Quantos números você quer digitar: ");
        int quant = input.nextInt();
        double[] array = new double[quant];
        double maiorN = 0.0;
        for (int i = 0; i < array.length; i++) {
            System.out.print("Digite um número: ");
            array[i] = input.nextDouble();
        }
        for (int i = 0; i < array.length; i++) {
            if (array[i] > maiorN) {
                maiorN = array[i];
            }
        }
        System.out.print("Maior número: ");
        System.out.println(maiorN);
        System.out.print("O maior número está na posição");
        for (int i = 0; i < array.length; i++) {
            if (maiorN == array[i]){
                System.out.print(" "+ i + " do elemento");
            }
        }

    }
}
