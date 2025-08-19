import java.util.Scanner;

public class Exercicio01 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();

        System.out.println("O número: "+ numero);

        if (numero >0) {
            System.out.println("O número é positivo");
        }
        else {
            System.out.println("O valor é negativo");
        }


    }
}
//Fazer um programa para ler um número inteiro, e depois dizer se este número é negativo ou não.
