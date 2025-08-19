package execucao;

import entities.Department;
import entities.HourContract;
import entities.Worker;
import entities.WorkerLevel;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args)throws ParseException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        System.out.print("Entre com o nome do departamento: ");
        String departmentName = sc.nextLine();

        System.out.println("Sua data: ");

        System.out.print("Name: ");
        String workerName = sc.nextLine();

        System.out.println("Level ");
        String workerLevel = sc.nextLine();

        System.out.println("Base salarial: ");
        double baseSalary = sc.nextDouble();

        Worker worker = new Worker(workerName,WorkerLevel.valueOf(workerLevel),baseSalary,new Department(departmentName));
        //Department department = new Department();

        System.out.println("Quantos contratos esse trabalhador vai ter: ");
        int nContratos = sc.nextInt();

        for (int contador= 1; contador <= nContratos; contador++){
            System.out.println("Entre com contratos " + contador + "data: ");
            System.out.print("Date (DD/MM/YYYY): ");
            Date contractDate = sdf.parse(sc.next());

            System.out.print("Valor por hora: ");
            double valuePerHour = sc.nextDouble();

            System.out.println("Duração (horas) ");
            int hours = sc.nextInt();

            HourContract contract = new HourContract(contractDate,valuePerHour,hours);
            worker.addContract(contract);

        }
        System.out.println();
        System.out.println("Entre com o mês e ano (MM/YYYY) para calcular o salário:  ");
        String mothAndYear = sc.next();

        int month = Integer.parseInt(mothAndYear.substring(0,2));
        int year = Integer.parseInt(mothAndYear.substring(3));

        System.out.println("Name: " + worker.getName());

        System.out.println("Departamento: " + worker.getDepartment().getName());

        sc.close();

        System.out.println("Renda por " + ":" + String.format("%.2f",worker.income(year,month)));
    }
}
