package java_introdução.curso_programacao;

import java.util.Locale;
import java.util.Scanner;

public class ex6_introdução2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double numero;

        numero = sc.nextDouble();
        if (numero <= 25) {
            System.out.println("Intervalo (0,25)");}

        else if (numero > 25 && numero <= 50) {
            System.out.println("Intervalo (25,50)");}

        else if (numero > 50 && numero <= 75){
            System.out.println("Intervalo (50,75)");}

        else if (numero > 75 && numero <= 100){
            System.out.println("Intervalo 75,100");}

        else{
            System.out.println("Fora dos intervalos");
        }
    }
}
