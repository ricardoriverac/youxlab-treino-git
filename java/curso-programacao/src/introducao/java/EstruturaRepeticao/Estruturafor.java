package introducao.java.EstruturaRepeticao;

import java.util.Scanner;

public class Estruturafor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x;
        int N = sc.nextInt();
        int soma = 0;
        for (int i = 0; i < N ; i++){
            x = sc.nextInt();
            soma += x;
        }
        System.out.println(soma);
    }
}
