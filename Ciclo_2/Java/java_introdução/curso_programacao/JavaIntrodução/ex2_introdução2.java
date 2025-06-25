package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex2_introdução2 {
    public static void main(String[] args) {
        int numero;
        Scanner sc = new Scanner(System.in);

        numero = sc.nextInt();

        if (numero % 2 == 0){
            System.out.println("Número par");
        }
        else{
            System.out.println("Número Ímpar");
        }
    }
}
