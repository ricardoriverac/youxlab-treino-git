package java_introdução.curso_programacao;

import java.util.Locale;
import java.util.Scanner;

public class ex5_introdução2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc =  new Scanner(System.in);

        int qtd, cod;

        cod = sc.nextInt();
        qtd = sc.nextInt();
        double total;

        if (cod == 1) {total = qtd * 4.00;}
        else if (cod == 2){ total = qtd * 4.50;}
        else if (cod == 3){ total = qtd * 5.00;}
        else if (cod == 4){ total = qtd * 2.00;}
        else { total = qtd * 1.50; }

        System.out.printf("Se vai ter que pagar $%.2f", total);

        sc.close();
        }
}
