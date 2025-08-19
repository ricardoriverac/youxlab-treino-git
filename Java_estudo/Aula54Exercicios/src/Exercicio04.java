import java.util.Scanner;

public class Exercicio04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();

        for (int contador = 0; contador < numero; contador++) {
            int valor1 = sc.nextInt();
            int valor2 = sc.nextInt();

            if (valor1 % 2 == 0 && valor2 % 2 == 0) {
                System.out.println("A divisão sera realizada ");
                int divisao = valor1/valor2;
                System.out.println(divisao);
            }
            else {
                System.out.println("A divisão não atende os critérios ");
            }
        }
        sc.close();
    }
}