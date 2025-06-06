package introducao.java.exercicios;

import java.util.Locale;

public class Exercicio1_c {
    public static void main(String[] args) {
        /// Concatenando Dados
        Locale.setDefault(Locale.US);
        String produtc1 = "computer";
        String produtc2 = "office desk";

        int age = 30;
        int code = 5290;
        char gender = 'F';

        double price1 = 2100.0;
        double price2 = 650.50;
        double measure = 53.2345;

        System.out.println("Product 1:");
        System.out.printf("%s, which price is %.2f %n" , produtc1 , price1);
        System.out.println("Product 2:");
        System.out.printf("%s, which price is %.2f %n" , produtc2 , price2);
        System.out.println();
        System.out.printf("Record: %d years old, code %d and gender: %s %n" , age , code , gender);
        System.out.printf("Measure with eight decimal places: %f %n",  measure );
        System.out.printf("Rouded (three decimal places): %.2f" , measure);
    }
}
