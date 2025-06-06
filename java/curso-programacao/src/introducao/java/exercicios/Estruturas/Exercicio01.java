package introducao.java.exercicios.Estruturas;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio01 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double nota1 , nota2;
        nota1 = sc.nextDouble();
        nota2 = sc.nextDouble();

        double resultado = nota1 + nota2;

        System.out.printf("Nota final: %.1f %n" , resultado);
        if (resultado < 60){
            System.out.println("RERPOVADO");
        }
        sc.close();
    }
}
