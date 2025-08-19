package execucao;

import Entidades.Account;
import Entidades.BusinessAccont;
import Entidades.SavingsAccount;

import java.util.ArrayList;
import java.util.List;

public class ProgramaAbstrata {
    public static void main(String[] args) {
        List<Account> list = new ArrayList<>();

        list.add(new SavingsAccount(1001, "Alex", 500.0, 0.01));
        list.add(new BusinessAccont(1002, "Maria", 1000.0, 400.0));
        list.add(new SavingsAccount(1003, "Amanda", 600.0, 0.02));
        list.add(new BusinessAccont(1004, "Joao", 2000.0, 300.0));

        double sum = 0.0;
        for (Account acc : list){
            sum += acc.getBalance();

        }
        System.out.printf("Total balance: %.2f%n",sum);

        for (Account acc: list){
            acc.deposit(10.0);
        }
        for (Account acc: list){
            System.out.println(acc.getBalance());
        }
    }
}