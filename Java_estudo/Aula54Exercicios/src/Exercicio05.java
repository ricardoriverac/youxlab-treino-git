import java.util.Scanner;

public class Exercicio05 {
    public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);

            int n = sc.nextInt();

            int fat = 1;
            for (int contador=1; contador<=n; contador++) {
                fat = fat * contador;
            }

            System.out.println(fat);

            sc.close();
        }
    }
