package introducao.poo.abstrant.exercicies.aplication;

import introducao.poo.abstrant.exercicies.entities.Company;
import introducao.poo.abstrant.exercicies.entities.Individual;
import introducao.poo.abstrant.exercicies.entities.TaxPayer;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class aplicationCompany {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        List<TaxPayer> taxPayers = new ArrayList<>();

        System.out.print("Enter the number of taxpayers: ");
        int quant = input.nextInt();
        for (int i = 0; i < quant; i++) {
            System.out.printf("Taxpayer #%d data: %n" , (i+1));
            System.out.print("Individual or Company (c/i): ");
            char resp = input.next().charAt(0);
            input.nextLine();
            System.out.print("Name: ");
            String name = input.nextLine();
            System.out.print("Anual income: ");
            double anualincome = input.nextDouble();
            if (resp == 'i'){
                System.out.print("Health expenditures: ");
                Double heatlhexpeen = input.nextDouble();
                taxPayers.add(new Individual(name , anualincome , heatlhexpeen));
            } else {
                System.out.print("Number of employees: ");
                Integer quantyemployees = input.nextInt();
                taxPayers.add(new Company(name , anualincome , quantyemployees));
            }
        }
        System.out.println();
        System.out.println("Taxes PAID:");
        for (TaxPayer tp : taxPayers) {
            System.out.println(tp.getName() + ": $" + String.format("%.2f" ,tp.tax()));
        }
        System.out.println();
        double sum = 0.0;
        for (TaxPayer payer : taxPayers) {
            sum += payer.tax();
        }
        System.out.print("Total taxes: " + String.format("%.2f",sum));




        input.close();
    }
}
