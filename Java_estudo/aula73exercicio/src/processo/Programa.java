package processo;

import entidade.Dollar;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Me diga a quantidade de dollar que deseja: ");
        Dollar.quantidade = sc.nextDouble();

        System.out.println("Me diga o valor do dollar: ");
        Dollar.valorDollar = sc.nextDouble();

        System.out.println(Dollar.CotacaoTotal());

        sc.close();
    }
}
