import java.util.Scanner;

public class Exercicio02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();

        for (int x = 1; x < numero;x++ ){
            if (x >= 10 && x <= 20) {
                System.out.println("O valor a seguir está dentro do intervalo: " + x);
            }
             else
                 System.out.println("Esse valor não está: " + x);

            }
        sc.close();
        }

    }

