package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex02_introdução {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double pi = 3.14159;
        double x;

        System.out.println("Vamos calcular um circulo");
        x = sc.nextDouble();

        double quadrado = x * x;
        double calculo = pi * quadrado;

        System.out.printf("A= %.4f",calculo);
        sc.close();


    }
}
