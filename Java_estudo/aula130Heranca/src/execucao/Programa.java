package execucao;

import Entidades.Account;
import Entidades.BusinessAccont;
import Entidades.SavingsAccount;

public class Programa {
    public static void main(String[] args) {
        Account acc = new Account(1001, "Alex", 0.0);

        BusinessAccont bcc = new BusinessAccont(1002, "Maria", 0.0, 500.0);

        //UPCASTING Pegar um objeto de uma subclasse e atribuir para a superClasse
        Account acc1 = bcc;
        Account acc2 = new BusinessAccont(1003, "Bob", 0.0, 200.0);
        Account acc3 = new SavingsAccount(1004, "Ana", 0.0, 0.01);

        //DOWNCASTING

        BusinessAccont acc4 = (BusinessAccont) acc2;
        acc4.loan(100);

        //BusinessAccont acc5 = (BusinessAccont)acc3;

        if (acc3 instanceof BusinessAccont) {
            BusinessAccont acc5 = (BusinessAccont) acc3;
            acc5.loan(200.0);
            System.out.println("Loan! ");
        }

        if (acc3 instanceof SavingsAccount) {
            SavingsAccount acc5 = (SavingsAccount) acc3;
            acc5.updateBalance();
            System.out.println("Update!");
        }

    }
}