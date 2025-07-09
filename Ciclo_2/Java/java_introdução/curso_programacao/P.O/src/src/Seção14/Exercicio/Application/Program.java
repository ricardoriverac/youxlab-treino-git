package Seção14.Exercicio.Application;

import Seção14.Exercicio.Entities.Account;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        Account account = new Account();

        System.out.println("Enter account data");
        System.out.print("Number: ");
        int number = input.nextInt();

        input.nextLine();

        System.out.print("Holder (Nome): ");
        String holder = input.nextLine();

        System.out.print("Saldo inicial: ");
        double balance = input.nextDouble();

        System.out.print("Limite de saque: ");
        double withdrawLimit = input.nextDouble();

        System.out.print("Quanto você quer sacar?: ");
        double withdraw = input.nextDouble();

        Account acc1 = new Account(number, holder, balance, withdrawLimit);

        account.withdraw(withdraw, withdrawLimit, balance);


    }
}
