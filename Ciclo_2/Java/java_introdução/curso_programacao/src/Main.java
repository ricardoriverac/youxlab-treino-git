package java_introdução.curso_programacao.src;

import java.util.Locale;

public class Main {
    public static void main(String[] args) {


        double x = 10.35784;
        String nome = "Garcia";
        int idade = 17;
        double renda = 300.0;
        System.out.println(x);
        System.out.printf("%.2f%n", x);
        Locale.setDefault(Locale.US);
        System.out.printf("%.2f%n", x);
        System.out.println(("Resultado = " + x + " Metros"));
        System.out.printf("Resultado = %.2f metros%n", x);
        System.out.printf("%s Tem %d anos e ganha R$ %.2f reais %n", nome, idade, renda);
    }

}


