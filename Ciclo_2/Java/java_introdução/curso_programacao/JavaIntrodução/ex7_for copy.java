package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex7_for {
    public static void main(String[] args) {

            Scanner input = new Scanner(System.in);

            int n = input.nextInt();

            for (int i=1; i<=n; i++) {

                int primeiro = i;
                int segundo = i * i;
                int terceiro = i * i * i;
                System.out.printf("%d %d %d%n", primeiro, segundo, terceiro);
            }

            input.close();
        }
    }
