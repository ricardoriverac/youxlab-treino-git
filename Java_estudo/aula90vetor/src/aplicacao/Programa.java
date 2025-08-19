package aplicacao;

import entidade.Produto;

import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        int numero = sc.nextInt();
        Produto[] vect = new Produto[numero];

        for(int contador =0;contador< vect.length;contador++){
            sc.nextLine();
            System.out.print("Digite o seu nome: ");
            String nome = sc.nextLine();
            double preco = sc.nextDouble();
            vect[contador] = new Produto(nome,preco);
        }

        double soma = 0;
        for (int contador = 0; contador <vect.length;contador++){
            soma += vect[contador].getPreco();
        }
        double media = soma / vect.length;

        System.out.printf("O preco é: = %.2f%n ",media);

        sc.close();

    }
}
