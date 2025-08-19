import java.util.Scanner;

public class Exercicio01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int senha = sc.nextInt();

        while (senha != 2000){
            System.out.println("Senha invalida");
            senha = sc.nextInt();
        }

        sc.close();
    }
}
