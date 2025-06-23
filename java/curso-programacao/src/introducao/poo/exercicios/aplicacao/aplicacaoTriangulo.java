package introducao.poo.exercicios.aplicacao;


import introducao.poo.exercicios.entities.Triangulo;

import java.util.Locale;
import java.util.Scanner;

public class aplicacaoTriangulo {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Triangulo triangulo = new Triangulo();
        System.out.println("De a entrada de um triângulo ");
        System.out.print("Largura ");
        triangulo.largura = sc.nextDouble();
        System.out.print("Altura ");
        triangulo.altura = sc.nextDouble();
        System.out.println("Area = " + triangulo.area());
        System.out.println("Perimetro = " + triangulo.perimetro());
        System.out.println("Diagonal = " + triangulo.diagonal());
        sc.close();
    }
}
