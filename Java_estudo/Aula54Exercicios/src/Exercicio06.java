import java.util.Scanner;

public class Exercicio06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numero = sc.nextInt();
        for (int contador = 1; contador < numero; contador++) {
            if (numero % contador == 0) {
                System.out.println(contador);

            }
        }
    }
}
