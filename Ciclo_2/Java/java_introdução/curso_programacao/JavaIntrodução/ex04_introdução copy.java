package java_introdução.curso_programacao;

import java.util.Locale;
import java.util.Scanner;

public class ex04_introdução {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int numero, horas;
        double valorHora, salario;

        numero = sc.nextInt();
        horas = sc.nextInt();
        valorHora = sc.nextDouble();

        salario = valorHora * horas;

        System.out.println("NUMBER = " + numero);
        System.out.printf("SALARY = U$ %.2f%n", salario);

        sc.close();
    }}
