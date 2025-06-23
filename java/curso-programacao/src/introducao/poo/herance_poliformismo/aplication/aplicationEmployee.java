package introducao.poo.herance_poliformismo.aplication;

import introducao.poo.herance_poliformismo.entities.Employee;
import introducao.poo.herance_poliformismo.entities.OutsourcedEmployee;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class aplicationEmployee {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        List<Employee> employees = new ArrayList<>();

        System.out.print("Enter the number of employees: ");
        int quant = input.nextInt();
        for (int i = 0; i < quant; i++) {
            System.out.println("Employee #" + (i+1) + " data:");
            System.out.print("Outsourced (y/n)? ");
            char enter = input.next().charAt(0);
            input.nextLine();
            System.out.print("Name: ");
            String name = input.nextLine();
            System.out.print("Hours: ");
            int hours = input.nextInt();
            System.out.print("Value per Hour: ");
            double valueperhour = input.nextDouble();
            if (enter == 'S' || enter == 's'){
                System.out.print("Additional charge: ");
                double additional = input.nextDouble();
                Employee emps = new OutsourcedEmployee(name , hours , valueperhour , additional);
                employees.add(emps);
            }
            else {
                Employee emps = new Employee(name ,  hours , valueperhour);
                employees.add(emps);
            }
        }
        System.out.println();
        System.out.println("PAYMENT: ");
        for (Employee employee : employees) {
            System.out.println("Name: " + employee.getName() + " - " + String.format("%.2f" , employee.payment()));
        }

    }
}
