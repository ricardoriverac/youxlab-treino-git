import java.util.Scanner;

public class Exercicio08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double salario = sc.nextDouble();

        double imposto = 0;

        if (salario <= 2000) {
            System.out.println("Você está isento");
        } else if (salario <= 4500) {
            imposto = (salario * 8) / 100 + salario;
        }
        else {
            imposto = (salario * 25)/100 + salario;
        }

            System.out.printf("R$ %.2f%n", imposto);

        sc.close();
    }
}