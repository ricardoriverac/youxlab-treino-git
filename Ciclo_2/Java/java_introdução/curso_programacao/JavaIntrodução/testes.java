package java_introdução.curso_programacao;

import javax.xml.crypto.dom.DOMCryptoContext;
import java.util.Locale;
import java.util.Scanner;

public class testes {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double largura = sc.nextDouble();
        double comprimento = sc.nextDouble();
        double metroQuadrado = sc.nextDouble();

        double area = largura * comprimento;
        double preco = metroQuadrado * area;

        System.out.printf("ÁREA = %.2f%n", area);
        System.out.printf("PRECO =  %.2f%n", preco);

        sc.close();
    }
}