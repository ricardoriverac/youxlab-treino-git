package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex4_introdução2 {
    public static void main(String[] args) {
        int dia = 24;
        Scanner sc = new Scanner(System.in);

        int horas = sc.nextInt();
        int horas2 = sc.nextInt();

        int duracao;
        if (horas < horas2) {
            duracao = horas2 - horas;
        }
        else {
            duracao = 24 - horas + horas2;
        }

        System.out.println("O JOGO DUROU " + duracao + " HORA(S)");

        sc.close();
    }
}
