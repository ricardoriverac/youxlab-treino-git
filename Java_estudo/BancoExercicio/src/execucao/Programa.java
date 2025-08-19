package execucao;

import entidades.Banco;
import entidades.ContaBancaria;
import entidades.Usuario;

import java.util.Random;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {

        Banco banco1 = new Banco();
        banco1.setNome("Banco Santander ");
        banco1.setCep(12345);

        Banco banco2 = new Banco();
        banco2.setNome("Banco do Brasil ");
        banco2.setCep(35324);

        ContaBancaria contaBancaria = new ContaBancaria();
        contaBancaria.setNomeTitular("Nicolas");

        ContaBancaria contaBanco1 = new ContaBancaria();
        contaBanco1.setNomeTitular("Nicolas");
        //contaBanco1.setNumeroConta(1111);
        //contaBanco1.setSaldo(5000.0);

        banco1.setContaBancaria(contaBancaria);

        System.out.println(banco1);

        Banco bancoBrasil = new Banco();




    }
}