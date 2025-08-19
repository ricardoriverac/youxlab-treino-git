package execucao;

import entidade.Medidas;

import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        int numero = sc.nextInt();
        Medidas[] vect = new Medidas[numero];

        for(int contador = 0;contador< vect.length;contador++){
            sc.nextLine();
            System.out.println("Digite seu nome: ");
            String nome = sc.nextLine();
            int idade = sc.nextInt();
            double altura = sc.nextDouble();
            vect[contador] = new Medidas(nome,idade,altura);
        }

        for (Medidas medidas : vect) {
            System.out.println(medidas);
        }


    }
}
