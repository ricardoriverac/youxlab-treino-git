package aplicacao;

import entidade.Banco;

import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        System.out.print("Me diga o número de sua conta: ");
        int contaNumero = sc.nextInt();

        sc.nextLine();
        System.out.print("Qual seu nome: ");
        String nomeUsuario = sc.nextLine();

        System.out.print("Informe seu saldoInicial ");
        double saldoInicialPrograma = sc.nextInt();

        Banco banco = new Banco(contaNumero,nomeUsuario);
        banco.setSaldoInicial(saldoInicialPrograma);

        System.out.println("Numero da conta: " + banco.getContaNumero());
        System.out.println("Nome: " + banco.getNomeUsuario());
        System.out.println("Seu saldo é: " + banco.getSaldo());

        System.out.print("O valor que deseja retirar ou adicionar em sua conta: ");
        double valor = sc.nextDouble();

        double novoSaldo = banco.transacaoBancaria(valor);
        System.out.println(novoSaldo);

    }
}
