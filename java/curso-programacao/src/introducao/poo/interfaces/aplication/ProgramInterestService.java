package introducao.poo.interfaces.aplication;

import introducao.poo.interfaces.model3.entities.BrazilInterestService;

import java.util.Locale;
import java.util.Scanner;

public class ProgramBrazil {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Amount: ");
        double amount = input.nextDouble();
        System.out.print("Months: ");
        int months = input.nextInt();

        BrazilInterestService is = new BrazilInterestService(2.0);

        double payment = is.payment(amount , months);
        System.out.println("O emprestimo feito em " + months + " meses tem o valor de.");
        System.out.printf("%.2f%n",payment);
    }
}
