package introducao.java.exercicios.Estruturas;

import java.util.Locale;
import java.util.Scanner;

public class Exe01 {
    public static void main(String[] args) {
        /// Fazer um programa para ler um número inteiro, e depois dizer se este número é negativo ou não.
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int a;
        a = sc.nextInt();
        if (a < 0)
            System.out.println("NEGATIVO");
        else
            System.out.println("NÂO NEGATIVO");
        sc.close();
    }
}
