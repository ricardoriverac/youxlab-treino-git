package introducao.poo.herance_poliformismo.aplication;

import introducao.poo.herance_poliformismo.entities.Account;
import introducao.poo.herance_poliformismo.entities.BusineesAccount;
import introducao.poo.herance_poliformismo.entities.SavingsAccount;

public class program {
    public static void main(String[] args) {

        Account acc = new Account(1001 , "Alex" , 0.0);
        BusineesAccount bacc = new BusineesAccount(1002 , "Titular" , 1200.0 , 3000.0);

        // UPCASTING e pegar um objeto de subClasse e atribui a ela uma superClasse(ClasseBase)
        Account acc1 = bacc;
        Account acc2 = new BusineesAccount(300 , "Bob" , 2000.0 , 3000.0);
        Account acc3 = new SavingsAccount(1003, "Anna" , 0.0 , 3000.0);

        //DOWNCASTING converte um objeto de superClasse para subclasse

        BusineesAccount acc4 =
                // O compilador não deixa eu atribui uma superclasse para subclasse
                // Devo fazer um casting manual
                (BusineesAccount)acc2;
        acc4.loan(100.0);

        // Como evitar de tipo de erro de atribui uma subclasse a outro subclasse BusineesAccount acc5 = (BusineesAccount)acc3;
        if (acc3 instanceof BusineesAccount){
            BusineesAccount acc5 = (BusineesAccount)acc3;
            acc5.loan(200.0);
            System.out.println("Loan!");
        }
        if (acc3 instanceof  SavingsAccount){
            SavingsAccount acc5 = (SavingsAccount)acc3;
            acc5.updateBalance();
            System.out.println("UPDATE");
        }
    }
}
