package execucao;

import entidade.enums.Cor;
import entidades.Circulo;
import entidades.Forma;
import entidades.Retangulo;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;


public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Forma> list = new ArrayList<>();

        System.out.println("Entre com o número de formas: ");
        int quantidade = sc.nextInt();

        for (int contador = 1; contador <= quantidade; contador++) {
            System.out.println("Forma # " + contador + " :");

            System.out.println("Retangulo ou circulo:(r/c) ");
            char escolhaForma = sc.next().charAt(0);

            System.out.println("Color [BLACK/BLUE/RED]: ");
            Cor cor = Cor.valueOf(sc.next());

            if (escolhaForma == 'r') {
                System.out.println("Largura: ");
                double largura = sc.nextDouble();

                System.out.println("Altura: ");
                double altura = sc.nextDouble();
                list.add(new Retangulo(cor, largura, altura));
            } else {
                System.out.println("Raio: ");
                double raio = sc.nextDouble();
                list.add(new Circulo(cor, raio));
            }


        }

        System.out.println();
        System.out.println("Forma areas: ");
        for (Forma forma : list) {
            System.out.println(String.format("%.2f",forma.area()));
        }
        sc.close();
    }

}