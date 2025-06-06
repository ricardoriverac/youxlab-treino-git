package introducao.java.exercicios.Sequencial;

import java.util.Scanner;

public class Exercicio1 {
    public static void main(String[] args) {
        // Faça um programa para ler dois valores inteiros, e depois mostrar na tela a soma desses números com uma
        //mensagem explicativa, conforme exemplos.
        Scanner sc = new Scanner(System.in);

        int valor1 = sc.nextInt();
        int valor2 = sc.nextInt();

        int resultado = valor1 + valor2;

        System.out.printf("A soma do valores %d e %d são %d" , valor1 , valor2 , resultado);
    }
}
