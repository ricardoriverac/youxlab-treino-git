package introducao.poo.exececoes.exercicies.aplication;

import introducao.poo.exececoes.exercicies.entities.Account;
import introducao.poo.exececoes.exercicies.entities.DomainExcpetion01;

import java.util.Locale;
import java.util.Scanner;

public class aplicationAccount {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);


        System.out.println("Enter account data");
        System.out.print("Number: ");
        int numberId = input.nextInt();
        System.out.print("Holder: ");
        input.nextLine();
        String name = input.nextLine();
        System.out.print("Initial balance: ");
        double balance = input.nextDouble();
        System.out.print("Withdraw Limit: ");
        double limitWith = input.nextDouble();
        Account account = new Account(numberId , name , balance , limitWith);

        System.out.print("Enter amount for withdraw: ");
        double withdraw = input.nextDouble();
        try {
            account.withdraw(withdraw);
            System.out.println("New balance: "+account.getBalance());

        }catch (DomainExcpetion01 errorArgs){
            System.out.println(errorArgs.getMessage());
        }
    }
}
