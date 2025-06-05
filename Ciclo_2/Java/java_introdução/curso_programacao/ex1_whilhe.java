package java_introdução.curso_programacao;

import java.util.Scanner;

public class ex1_whilhe {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite sua senha!");

        int senha = input.nextInt();

        while (senha != 2002){
            System.out.println("Senha inválida, digite novamente");
            senha = input.nextInt();
        }
        System.out.println("Senha correta!");
    }

}
