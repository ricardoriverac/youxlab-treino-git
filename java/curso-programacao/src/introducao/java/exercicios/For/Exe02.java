package introducao.java.exercicios.For;

import java.util.Scanner;

public class Exe02 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int quant = input.nextInt();
        int in = 0;
        int out = 0;
        for (int i = 0; i < quant; i++) {
            int valor = input.nextInt();
            if (valor < 0 || valor > 20 ){
                out += 1;
            }
            else {
                in++;
            }
        }
        System.out.println("in " + in);
        System.out.println("out " + out);
    }
}
