package java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.aplication;

import java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.ultil.aula81_ultil;

import java.util.Locale;
import java.util.Scanner;

public class aula81_aplication {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        int option = 0;

        System.out.print("Enter account number: ");
        int number = input.nextInt();
        System.out.print("Enter account holder: ");
        input.nextLine();
        String holder = input.nextLine();
        System.out.print("Is there an initial deposit (y/n)? ");
        char response = input.next().charAt(0);
        aula81_ultil aula81_ultil;
        if (response == 'y') {
            System.out.print("Enter initial deposit value: ");
            double initialDeposit = input.nextDouble();
            aula81_ultil = new aula81_ultil(number, holder, initialDeposit);
        } else {
            aula81_ultil = new aula81_ultil(number, holder);
        }

        while (option != 4) {
            System.out.println("what would you like to do?");
            System.out.println(" (1) See the status of my account \n (2) Deposit an amount \n (3) Remove a value \n (4) End the program");
            option = input.nextInt();


            if (option == 1) {
                System.out.println();
                System.out.println("Account data: ");
                System.out.println(aula81_ultil);
                System.out.println();
            } else if (option == 2) {
                System.out.println();
                System.out.print("Enter a deposit value: ");
                double depositValue = input.nextDouble();
                aula81_ultil.deposit(depositValue);
                System.out.println();
            } else if (option == 3) {
                System.out.println();
                System.out.print("Enter a withdraw value: ");
                double withdrawValue = input.nextDouble();
                aula81_ultil.withdraw(withdrawValue);
                System.out.println();
            }
            else {
                System.out.println("We don't have the option: " + option);
                System.out.println();
            }
        }

        System.out.println("Thank you for using our bank, see you later!");
        input.close();

    }


}
