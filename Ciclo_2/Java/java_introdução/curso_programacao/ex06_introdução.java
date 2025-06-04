package java_introdução.curso_programacao;

import java.util.Locale;
import java.util.Scanner;

public class ex06_introdução {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double pi = 3.14159;
        double n1, n2, n3, areaT;

        n1 = sc.nextDouble();
        n2 = sc.nextDouble();
        n3 = sc.nextDouble();

        areaT = n1 * n3 / 2;
        System.out.printf("A área do triangulo é: %.3f", areaT);

        double quadrado = n3 * n3;
        double calculo = pi * quadrado;
        System.out.printf("%nCirculo: %.3f",calculo);

        double calculoTra1 = ((n1 + n2) * n3) / 2;
        System.out.printf("%nTrapezio%.3f",calculoTra1);

        double quadrado2 = n2 * n2;
        System.out.printf("%nQuadrado %.3f", quadrado2);

        System.out.printf("%nRetangulo: %.2f", n1 * n2);
    }


}
