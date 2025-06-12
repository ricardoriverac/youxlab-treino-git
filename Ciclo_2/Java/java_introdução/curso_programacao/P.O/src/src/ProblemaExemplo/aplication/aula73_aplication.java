package java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.aplication;

import java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.ultil.aula73_ultil;

import java.util.Locale;
import java.util.Scanner;

public class aula73_aplication {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        aula73_ultil dollar = new aula73_ultil();

        System.out.print("Qual o preço do dolar hoje?: ");
        dollar.dollarPrice = input.nextDouble();

        System.out.print("Quantos dolars você gostaria de trocar para R$?: ");
        dollar.dollarqtd = input.nextDouble();

        System.out.printf("Já com a taxa você ira receber : %.2f", dollar.CurrencyConverter());



    }
}
