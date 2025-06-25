package java_introdução.curso_programacao;

import java.util.Locale;

public class Parte2 {
    public static void main(String[] args) {
        String product1 = "Computer";
        String product2 = "Office Desk";
        int age = 30;
        int code = 5290;
        char gender = 'F';
        double price1 = 2100.0;
        double price2 = 650.50;
        double measure = 53.234567;

        System.out.printf("Products:%n%s, which price is $%.2f %n%s, which price is $%.2f %n", product1, price1, product2, price2);

        System.out.println(" ");

        StringBuilder stringformatada = new StringBuilder();
        stringformatada.append(age).append(" years old, code ").append(code).append(" and gender ").append(gender);
        System.out.println(stringformatada.toString());

        System.out.println(" ");

        StringBuilder pt3 = new StringBuilder();
        pt3.append("Measure with eight decimal places: ").append( measure).append("\n").append("Rouded (three decimal places): ").append(String.format("%.2f", measure));
        System.out.println(pt3);

        Locale.setDefault(Locale.US);
        StringBuilder pt4 = new StringBuilder();
        pt4.append("US decimal point: ").append(String.format("%.2f", measure));
        System.out.print(pt4);

    }
}
