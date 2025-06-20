package introducao.poo.composition.aplication;

import introducao.poo.composition.enteties.Department;
import introducao.poo.composition.enteties.HourContrant;
import introducao.poo.composition.enteties.Worker;
import introducao.poo.composition.enteties.WorkerLevel;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;


public class aplicationWorker {
    public static void main(String[] args) throws ParseException {
        SimpleDateFormat fmt = new SimpleDateFormat("dd/MM/yyyy");
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Entre com nome do departamento: ");
        String depertament = input.nextLine();
        System.out.println("Entre com os dados do funcionário: ");
        System.out.print("Nome: ");
        String workerName = input.nextLine();
        System.out.print("Level: ");
        String workerLevel = input.nextLine();
        System.out.print("Base do salário: ");
        double baseSalary = input.nextDouble();
        Worker worker = new Worker(workerName , WorkerLevel.valueOf(workerLevel) , baseSalary , new Department(depertament));

        System.out.print("Quantos contratos tem o funcionário: ");
        int quant = input.nextInt();

        for (int i = 0; i < quant; i++) {
            System.out.println("Entre com #" + i+1 + " contrato");
            System.out.print("DATA (DD/MM/YYYY): ");
            Date contractDate = fmt.parse(input.next());
            System.out.print("Valor por hora: ");
            double valueperHour = input.nextDouble();
            System.out.print("Duração por horas: ");
            int hours = input.nextInt();
            HourContrant contrant = new HourContrant(contractDate , valueperHour , hours);
            worker.addContrant(contrant);

        }

        System.out.print("Entre com o mes e o ano para calcular a renda (MM/YYYY): ");
        String mes_ano = input.next();
        int mouth = Integer.parseInt(mes_ano.substring(0 ,2 ));
        int year = Integer.parseInt(mes_ano.substring(3));

        System.out.println("Nome: " + worker.getName());
        System.out.println("Departamento: " + worker.getDepartment().getName());
        System.out.println("A renda do mes " + mes_ano + " foi: " + worker.income(year , mouth));
    }
}
