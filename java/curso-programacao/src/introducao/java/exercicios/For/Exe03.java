package introducao.java.exercicios.For;

import java.util.Scanner;

public class Exe03 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Entre com quantidade: ");
        int quant = input.nextInt();
        for (int i = 0; i < quant; i++) {
            System.out.println("Enter case" + i);
            double valor1 = input.nextDouble();
            double valor2 = input.nextDouble();
            double valor3 = input.nextDouble();

            double media = ((valor1 * 2) + (valor2  * 3) + (valor3 * 5)) / 10;

            System.out.printf("Média ponderada %.2f %n",media);
        }
    }
}
