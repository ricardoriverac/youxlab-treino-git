package java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.aplication;

import java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.entities.ex2_entities;

import java.util.Locale;
import java.util.Scanner;

public class ex2_aplication {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        ex2_entities emp = new ex2_entities();

        System.out.print("Qual o seu nome?: ");
        emp.nome =  input.nextLine();
        System.out.print("Sálario Grosso?: ");
        emp.grossSalary = input.nextDouble();
        System.out.print("Tax?: ");
        emp.tax = input.nextDouble();

        System.out.println();
        System.out.println("Employee: " + emp);
        System.out.println();

        System.out.print("Which percentage to increase salary? ");
        double porcentage =  input.nextDouble();
        emp.increaseSalary(porcentage);

        System.out.println();
        System.out.println("Updated data: " + emp);
        input.close();


    }
}
