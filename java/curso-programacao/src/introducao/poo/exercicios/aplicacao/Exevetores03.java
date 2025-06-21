package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores03 {
    /// <h3 style= color:blue>Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
    /// tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
    /// bem como os nomes dessas pessoas caso houver.<h3/>
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        System.out.print("Quantas pessoas serão digitadas: ");
        int quant = input.nextInt();
        String[] nome = new String[quant];
        int[] idade = new int[quant];
        double[] altura = new double[quant];
        double soma = 0.0;
        int totaldemenos16 = 0;
        for (int i = 0; i < quant; i++) {
            input.nextLine();
            System.out.printf("Dados da %da pessoa:%n", i + 1);
            System.out.print("Nome: ");
            nome[i] = input.nextLine();
            System.out.print("idade: ");
            idade[i] = input.nextInt();
            if (idade[i] < 16) {
                totaldemenos16 += 1;
            }
            System.out.print("Altura: ");
            altura[i] = input.nextDouble();
            soma = soma + altura[i];
        }
        double avg = soma / altura.length;
        double porcetagem = ((double) totaldemenos16 / quant) * 100;
        System.out.printf("Altura Media: %.2f %n", avg);
        System.out.printf("Pessoas com menos de 16: %.1f%s %n", porcetagem, "%");
        for (int i = 0; i < quant; i++) {
            if (idade[i] < 16) {
                System.out.println(nome[i]);
            }
        }
        input.close();
    }
}