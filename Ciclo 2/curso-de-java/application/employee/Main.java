package application.employee;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Nome:");
        String name = sc.nextLine();

        System.out.println("salário bruto:");
        double gross = sc.nextDouble();

        System.out.println("Taxa:");
        double tax = sc.nextDouble();

        Employee emp = new Employee(name, gross, tax);

        System.out.printf("Employee: %s, $ %.2f%n", emp.getName(), emp.netSalary());

        System.out.println();
        System.out.println("Which percentage to increase salary?");
        double percent = sc.nextDouble();

        emp.increaseSalary(percent);

        System.out.printf("Updated data: %s, $ %.2f%n", emp.getName(), emp.netSalary());

        sc.close();
    }
}
