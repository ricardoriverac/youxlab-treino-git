package introducao.java.exercicios.Estruturas;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio03 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int a , b , c;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        if (a < b && a < c)
            System.out.println("Menor " + a);
        else if (b < c){
            System.out.println("Menor " + b);
        }
        else {
            System.out.println("Menor " + c);
        }
    }
}
