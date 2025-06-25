package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex03_introdução {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int q,w,e,r;
        q = sc.nextInt();
        sc.nextLine();
        w = sc.nextInt();
        sc.nextLine();
        e = sc.nextInt();
        sc.nextLine();
        r = sc.nextInt();

        int diferenca = q*w-e*r;
        System.out.println(diferenca);

        sc.close();
    }}
