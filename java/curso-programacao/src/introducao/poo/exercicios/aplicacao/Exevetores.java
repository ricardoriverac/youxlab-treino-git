package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores {
    ///  Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
    /// e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos.
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Quantos númros você vai digitar? ");
        int quantidade = input.nextInt();
        int [] array = new int[quantidade];
        for (int i = 0; i < array.length ; i++) {
            System.out.print("Digite um número: ");
            array[i] = input.nextInt();
        }
        for (int i = 0; i < array.length; i++) {
            if (array[i] < 0){
                System.out.println(array[i]);
            }
        }
    }
}