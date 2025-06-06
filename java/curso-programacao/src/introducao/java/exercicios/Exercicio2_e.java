package introducao.java.exercicios;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio2_e {
    /// Exercício com entrada de dados e saida
    public static void main(String[] args) {
        // OBS: O java ele reconhece o meu computador com o idioma português então para se quiser fazer calculos em ingles devo colocar em ingles com:

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double largura = sc.nextDouble();
        double comprimento = sc.nextDouble();
        double metroquadrado = sc.nextDouble();

        double area = largura * comprimento;
        double preco = area * metroquadrado;

        System.out.printf("Area: %.2f %n", area);
        System.out.printf("Preço: %.2f", preco);
        sc.close();
    }
}
