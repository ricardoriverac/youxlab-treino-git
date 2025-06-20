package introducao.poo.herance_poliformismo.aplication;

import introducao.poo.herance_poliformismo.entities.Account;
import introducao.poo.herance_poliformismo.entities.BusineesAccount;
import introducao.poo.herance_poliformismo.entities.SavingsAccount;

public class program02 {
    public static void main(String[] args) {
        Account acc1 = new Account(1001 , "alex" , 1000.0);
        acc1.withdraw(200.0);
        System.out.println(acc1.getBalance());

        Account acc2 = new SavingsAccount(1002 , "Maria" , 1000.0 , 0.0);
        acc2.withdraw(200.0);
        System.out.println(acc2.getBalance());

        Account acc3 = new BusineesAccount(1003 , "bob" , 1000.0 , 500.0);
        acc3.withdraw(200.0);
        System.out.println(acc3.getBalance());
    }
}
