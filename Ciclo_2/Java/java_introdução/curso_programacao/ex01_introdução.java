package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex01_introdução {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x, y;


        System.out.println("Digite dois números para eu somar");
        x = sc.nextInt();
        sc.nextLine();
        y = sc.nextInt();

        double soma = x+y;
        System.out.println("A soma é: "+soma);

        sc.close();

    }
}
