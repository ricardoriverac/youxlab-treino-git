package java_introdução.curso_programacao;

import java.util.Scanner;

public class estrutura_for {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int N, soma, i, x;


        N = input.nextInt();
        soma = 0;

        for (i=0; i<N; i++){
            x = input.nextInt();
            soma += x;
        }

        System.out.println(soma);

        input.close();

    }
}
