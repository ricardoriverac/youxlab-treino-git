import entities.Employee;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        System.out.print("Entre com o caminho: ");
        String path = input.nextLine();

        BufferedReader bw = new BufferedReader(new FileReader(path));
        String line = bw.readLine();

        List<Employee> employees = new ArrayList<>();
        while (line != null){
            String[] campos = line.split(",");
            employees.add(new Employee(campos[0] , campos[1] , Double.parseDouble(campos[2])));
            line = bw.readLine();
        }

        System.out.print("Entre com salário: ");
        double salary = input.nextDouble();
        List<String> namesEmails = employees.stream()
                .filter(e -> e.getSalary() >= salary)
                .map(x -> x.getEmail())
                .sorted((x1 , x2) -> x1.compareTo(x2))
                .toList();

        namesEmails.forEach(System.out::println);

        Double sum = employees.stream()
                .filter(x -> x.getName().charAt(0) == 'M' || x.getName().charAt(0) == 'm')
                .map(Employee::getSalary)
                .reduce( 0.0, Double::sum);

        System.out.println("Soma dos sálarios que começam com a letra 'M': " + sum);
    }
}