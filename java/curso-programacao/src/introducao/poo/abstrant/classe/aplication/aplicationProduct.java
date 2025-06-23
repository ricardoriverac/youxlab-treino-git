package introducao.poo.abstrant.classe.aplication;

import introducao.poo.abstrant.classe.entities.Account;
import introducao.poo.abstrant.classe.entities.BusineesAccount;
import introducao.poo.abstrant.classe.entities.SavingsAccount;

import java.util.ArrayList;
import java.util.List;

public class aplicationProduct {
    public static void main(String[] args) {

        List<Account> list = new ArrayList<>();

        list.add(new SavingsAccount(1001 , "Alex" , 500.00 , 00.1));
        list.add(new BusineesAccount(1001 , "Alex" , 500.00 , 100.00));
        list.add(new SavingsAccount(1001 , "Alex" , 500.00 , 00.2));
        list.add(new BusineesAccount(1001 , "Alex" , 500.00 , 500.00));
        double sum = 0.0;
        for (Account account : list) {
            sum += account.getBalance();
        }
        System.out.printf("Total balance %.2f %n" , sum);

        for (Account account2 : list) {
            account2.deposit(10.0);
        }

        for (Account account3 : list) {
            System.out.printf("Saldo atualizado para cada conta %d: %.2f %n" , account3.getNumber() , account3.getBalance());
        }


    }


}
