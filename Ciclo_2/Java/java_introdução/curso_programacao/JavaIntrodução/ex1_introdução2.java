package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex1_introdução2 {
    public static void main(String[] args) {
        int numero;
        Scanner sc = new Scanner(System.in);

        numero = sc.nextInt();
        if (numero < 0 ){
            System.out.println("Número negativo paizão");
        }
        else {
            System.out.println("Número positivo");
        }
    }
}
