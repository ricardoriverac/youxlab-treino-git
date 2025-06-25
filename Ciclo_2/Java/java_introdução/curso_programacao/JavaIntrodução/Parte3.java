package java_introdução.curso_programacao;

import java.util.Scanner;

public class Parte3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // para strings
        String x;
        x = sc.next();
        System.out.println("Você digitou " + x);

        // numeros inteiros
        int y;
        y = sc.nextInt();
        System.out.println("Você digitou " + y );

        // float
        double w;
        w = sc.nextDouble();
        System.out.println("Você digitou " + w );

        sc.close();
    }
}

//package java_introdução.curso_programacao;

//import java.util.Scanner;

//public class Parte3 {
    //public static void main(String[] args) {

      //  Scanner sc = new Scanner(System.in);

        //int x;
        //String s1, s2, s3;
        //x = sc.nextInt();
        //sc.nextLine();
        //s1 = sc.nextLine();
        //s2 = sc.nextLine();
        //s3 = sc.nextLine();

        //System.out.println("Dados Digitados");
        //System.out.println(x);
        //System.out.println(s1);
        //System.out.println(s2);
       // System.out.println(s3);


    //}
//}