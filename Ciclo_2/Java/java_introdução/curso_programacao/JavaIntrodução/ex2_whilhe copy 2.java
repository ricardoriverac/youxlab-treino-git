package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex2_whilhe {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int x = input.nextInt();
        int y = input.nextInt();

        while (x != 0 && y != 0) {

            if (x > 0 && y > 0 ){
                System.out.println("Primeiro quadrante");
            }
            else if (x < 0 && y > 0){
                System.out.println("Segundo quadrante");
            }
            else if (x < 0 && y < 0){
                System.out.println("Terceiro quadrante");
            }
            else if (x > 0 && y <0){
                System.out.println("Quarto quadrante");
            }
            x = input.nextInt();
            y = input.nextInt();

        }
        System.out.println("Digitou 0? Programa encerrado");
        input.close();
    }
}
