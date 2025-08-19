import java.util.Scanner;

public class Exercicio03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int escolha = sc.nextInt();
        String combustivel;

        while (escolha != 0) {
            switch (escolha) {
                case 1:
                    combustivel = "Gasolina";
                    break;
                case 2:
                    combustivel = "Diesel";
                    break;
                case 3:
                    combustivel = "Etanol";
                    break;
                default:
                    combustivel = "Valor inválido";

            }
            System.out.println(combustivel);
        }
        sc.close();
    }
}

