import java.util.Scanner;

public class Exercicio02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();

        if (numero % 2 == 0) {
            System.out.println("Seu valor é par ");
        }
        else {
            System.out.println("Seu valor é impar ");
        }

    }
}

//Fazer um programa para ler um número inteiro e dizer se este número é par ou ímpar.