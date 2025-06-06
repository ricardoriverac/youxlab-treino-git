package introducao.java.exercicios.Estruturas;

import java.util.Locale;
import java.util.Scanner;

public class Exe06 {
    /// Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos
    /// seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em
    /// nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double a;
        a = sc.nextDouble();
        if (a < 0 || a > 100)
            System.out.println("Erro ");
        else if (a <= 25)
            System.out.println("Valor encontradado entre 0 e 25");
        else if (a <= 50) {
            System.out.println("Valor encontradado entre 25 e 50");
        }
        else if (a <= 75){
            System.out.println("Valor encontradado entre 50 e 75");
        }
        else if (a <= 100)
            System.out.println("Valor encontradado entre 75 e 100");


    }


}
