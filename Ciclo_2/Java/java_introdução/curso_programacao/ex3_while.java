package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex3_while {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int alcool, gasolina, disel, gasosa;

        alcool = 0;
        gasolina = 0;
        disel = 0;


        gasosa = input.nextInt();

        while (gasosa != 4) {

            if (gasosa == 1) {
                alcool += 1;
            } else if (gasosa == 2) {
                gasolina += 1;
            } else if (gasosa == 3) {
                disel += 1;
            }
            gasosa = input.nextInt();

        }
        System.out.println("Muito obrigado");
        System.out.println("Alcool: " + alcool);
        System.out.println("Gasolina: " + gasolina);
        System.out.println("Disel: " + disel);
    }
}
