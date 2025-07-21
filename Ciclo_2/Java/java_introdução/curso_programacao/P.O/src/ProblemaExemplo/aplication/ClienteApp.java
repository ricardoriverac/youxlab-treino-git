package ProblemaExemplo.aplication;

import ProblemaExemplo.entities.PessoaParaCliente;

import java.util.*;

public class ClienteApp {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        List<PessoaParaCliente> lista = new ArrayList<>();

        System.out.println("How many employees will be registered?: ");
        int employees = input.nextInt();

        for (int i=0; i<employees; i++) {
            PessoaParaCliente pessoa = new PessoaParaCliente();
            System.out.println("Employee #" + i);

            System.out.print("ID: ");
            pessoa.id = input.nextInt();


            input.nextLine();
            System.out.print("Name: ");
            pessoa.name = input.nextLine();

            System.out.print("Salary: ");
            pessoa.salary = input.nextDouble();
            lista.add(pessoa);
        }

        System.out.print("Enter the employee id that will have salary increase: ");
        int idParaTaxa = input.nextInt();

        PessoaParaCliente pessoaSalva = lista.stream().filter(p -> p.getId() == idParaTaxa).findFirst().orElseGet(() -> null);

        if (pessoaSalva == null){
            System.out.println("This id does not exist!");
        }
        else {
            System.out.print("Enter the percentage: ");
            double taxa = input.nextDouble();
            double aumento = pessoaSalva.getSalary() * taxa / 100;
            pessoaSalva.setSalary(pessoaSalva.getSalary() + aumento);
        }

        System.out.println("\nList of employees:");
        for (PessoaParaCliente pessoa : lista) {
            System.out.println(pessoa);
        }

    }
}
