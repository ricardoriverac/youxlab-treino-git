package introducao.java.exercicios.Sequencial;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio3 {
    /// Fazer um programa para ler quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto
    /// de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int difirenca = (a * b - c * d);
        System.out.printf("Diferença: %d" , difirenca);
        sc.close();
    }
}
