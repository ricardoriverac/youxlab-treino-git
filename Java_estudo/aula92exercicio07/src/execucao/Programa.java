package execucao;

import entidade.Pessoa;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Me diga quantas vezes vai repetir: ");
        int numero = sc.nextInt();

        Pessoa[] vect = new Pessoa[numero];

        for (int contador =0;contador<numero;contador++){
            System.out.print("Escolha seu gênero [F/M]: ");
            char genero = sc.next().charAt(0);
            System.out.print("Seu nome: ");
            sc.nextLine();
            String nome = sc.nextLine();

            vect[contador] = new Pessoa(nome,genero);
        }
        for (int contador =0;contador<numero;contador++){
            System.out.println(vect[contador]);
        }
        sc.close();
    }

}
