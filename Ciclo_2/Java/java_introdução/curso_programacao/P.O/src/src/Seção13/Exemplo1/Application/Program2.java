package Seção13.Exemplo1.Application;

import Seção13.Exemplo1.Entites.Account;

public class Program2 {
    public static void main(String[] args) {

        Account acc1 = new Account(1001, "Alex", 1000.0) {
            @Override
            public void whithdraw(double amount) {

            }
        };

    }
}
