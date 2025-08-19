import java.util.Locale;
import java.util.Scanner;

public class exercicio03 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double A = sc.nextDouble();
        double B = sc.nextDouble();
        double C = sc.nextDouble();
        double D = sc.nextDouble();

        double diferenca = (A * B - C * D);

        System.out.printf(" O diferenca e %.2f%n ",diferenca);
        //Fazer um programa para ler quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto
        //de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
    }
}
