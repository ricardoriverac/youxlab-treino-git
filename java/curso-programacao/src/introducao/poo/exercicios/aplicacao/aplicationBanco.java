package introducao.poo.exercicios.aplicacao;

import introducao.poo.exercicios.entities.Conta;

import java.util.Locale;
import java.util.Scanner;

public class aplicationBanco {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        System.out.println("Banco da YouX");

        System.out.print("Numero da conta: ");
        int numeroConta = input.nextInt();

        input.nextLine();

        System.out.print("Usuário da conta: ");
        String nomeUsuario = input.nextLine();

        Conta conta = new Conta(numeroConta, nomeUsuario);

        System.out.print("Quer depositar um valor inicial? [S/N] ");
        char temvalorini = input.next().charAt(0);
        double deposito;
        if (temvalorini == 's' || temvalorini == 'S') {
            System.out.print("Insire o deposito inicial: ");
            deposito = input.nextDouble();
            conta.setSaldo(deposito);
        }
        System.out.println(conta);

        System.out.print("Deposite um valor: ");
        deposito = input.nextDouble();
        conta.depositar(deposito);
        System.out.println(conta);

        System.out.println("Saque um valor: ");
        double saque = input.nextDouble();
        conta.saque(saque);
        System.out.println(conta);
    }
}
