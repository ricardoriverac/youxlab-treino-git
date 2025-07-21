package ProblemaExemplo.aplication;

import ProblemaExemplo.entities.ex2_entities;

import java.util.Locale;
import java.util.Scanner;

public class ex2_aplication {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        ex2_entities emp = new ex2_entities();

        System.out.print("Qual o seu nome?: ");
        emp.nome =  input.nextLine();
        System.out.println("Sálario Grosso?: ");
        emp.grossSalary = input.nextDouble();
        System.out.println("Tax?: ");
        emp.tax = input.nextDouble();

        System.out.println();
        System.out.print(emp);
        System.out.println();

        double porcentage =  input.nextDouble();
        emp.increaseSalary(porcentage);


        System.out.println(emp);


    }
}
