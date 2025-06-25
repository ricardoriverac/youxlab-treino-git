package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex6_for {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        for (int i=1; i<=n; i++) {
            if (n % i == 0) {
                System.out.println(i);
            }
        }

        input.close();
    }
}
