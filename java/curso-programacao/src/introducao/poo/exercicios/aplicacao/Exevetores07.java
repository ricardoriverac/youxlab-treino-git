package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores07 {
    ///  <p style= color:purple> Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
    /// mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
    /// os elementos do vetor que estejam abaixo da média, com uma casa decimal cada. <p/>
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Quantos elementos vai ter o vetor: ");
        int quant = input.nextInt();
        double[] array = new double[quant];
        double soma = 0.0;
        for (int i = 0; i < array.length; i++) {
            System.out.print("Digite o número: ");
            array[i] = input.nextDouble();
            soma = soma + array[i];
        }
        double avg = soma / array.length;
        System.out.printf("Média do VETOR: %.3f %n" , avg);
        System.out.println("Elementos abaixo da média");
        for (int i = 0; i < array.length; i++) {
            if (array[i] < avg){
                System.out.println(array[i]);
            }
        }


    }
}
