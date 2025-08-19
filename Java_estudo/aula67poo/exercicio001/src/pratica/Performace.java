package pratica;

import entidade.Triangulo;

import java.util.Scanner;

public class Performace {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Triangulo triangulo = new Triangulo();
        System.out.print("Entre com o valor da base: ");
        triangulo.base = sc.nextInt();

        System.out.print("Entre com o valor da altura: ");
        triangulo.altura = sc.nextInt();

        System.out.println(triangulo.areaTriangulo());

        sc.close();
    }
}
