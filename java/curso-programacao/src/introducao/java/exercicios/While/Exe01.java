package introducao.java.exercicios.While;

import java.util.Scanner;

public class Exe01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x;
        int acesso = 2002;
        x = sc.nextInt();
        while (x != acesso){
            System.out.println("Senha invalida");
            x = sc.nextInt();
        }
        System.out.println("Acesso permitido");
    }
}
