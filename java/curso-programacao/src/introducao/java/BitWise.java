package introducao.java;

import java.util.Scanner;

public class BitWise {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // & e
        // | ou
        // ^ xor
        int mask = 0b100000;
        int x = sc.nextInt();
        if ((x & mask) != 0) {
            System.out.println("E o 6bit");
        }
        else
            System.out.println("Não e o 6bit");
    }
}
