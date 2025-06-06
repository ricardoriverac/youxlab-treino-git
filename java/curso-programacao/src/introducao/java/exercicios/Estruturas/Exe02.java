package introducao.java.exercicios.Estruturas;

import java.util.Locale;
import java.util.Scanner;

public class Exe02 {
    /// Fazer um programa para ler um número inteiro e dizer se este número é par ou ímpar.
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int a;
        a = sc.nextInt();
        if (a == 0)
            System.out.println("Você digitou um número nulo e ele e PAR");
        else if (a % 2 == 0)
            System.out.println("PAR");
        else
            System.out.println("IMPAR");
    }
}
