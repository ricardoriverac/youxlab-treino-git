package introducao.poo.herance_poliformismo.aplication;

import introducao.poo.herance_poliformismo.entities.Account;
import introducao.poo.herance_poliformismo.entities.SavingsAccount;


// Poliformismo significa muitas formas , siginifica que a mesma variável possa apontar
// para obejtos de tipos específicos , tendo comportamento diferente conforme cada tipo específico
public class program03 {
    public static void main(String[] args) {
        Account x = new Account(1001 , "Ana" , 1000.0);
        Account y = new SavingsAccount(1002 , "Maria" , 1000.0 , 00.1);

        x.withdraw(50.0);
        y.withdraw(50.0);

        System.out.println(x.getBalance());
        System.out.println(y.getBalance());

    }
}
