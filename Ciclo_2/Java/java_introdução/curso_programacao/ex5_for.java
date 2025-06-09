package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex5_for {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int fatorial = 1;

        int entrada = input.nextInt();

        for (int i = 1; i <= entrada; i++) {

            fatorial *= i;
        }
        System.out.println(fatorial);

    }
}