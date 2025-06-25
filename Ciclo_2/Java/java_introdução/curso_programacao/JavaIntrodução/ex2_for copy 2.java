package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex2_for {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n, x, i, in, out;

        in = 0;
        out = 0;

        n = input.nextInt();

        for (i = 0; i < n; i++) {
            x = input.nextInt();
            if (x > 9 && x < 21) {
                in += 1;
            } else {
                out += 1;
            }
        }
        System.out.println(in + " in");
        System.out.print(out + " out");



    }
}
