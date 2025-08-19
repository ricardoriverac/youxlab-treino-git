package execucao;

import entidade.ContaBancaria;
import exececoes.DomainException;

import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        try {


            System.out.println("Digite o número de sua conta bancária: ");
            int numeroConta = sc.nextInt();

            System.out.println("Digite seu saldo atual: ");
            double saldo = sc.nextDouble();

            ContaBancaria conta = new ContaBancaria(numeroConta, saldo);

            System.out.println("Digite o valor que deseja sacar ");
            double valorSacado = sc.nextDouble();

            System.out.println(conta.saque(valorSacado));
            System.out.println(conta.getSaldo());
            sc.close();
        } catch (DomainException excecao) {
            System.out.println("Erro ao realizar saque: " + excecao.getMessage());
        }
        sc.close();
    }

}