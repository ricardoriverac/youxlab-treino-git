package java_introdução.curso_programacao;

import java.util.Locale;
import java.util.Scanner;

public class do_whilhe {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        char resp;
        do {
            System.out.print("Digite a temperatura em Celsius: ");
            double C = input.nextDouble();
            double F = 9.0 * C / 5.0 + 32.0;
            System.out.printf("Equivalente em fairinhart: %.1f%n", F);
            System.out.print("Deseja repetir? (S/N) ");
            resp = input.next().charAt(0);
        } while (resp != 'N');



    }
}