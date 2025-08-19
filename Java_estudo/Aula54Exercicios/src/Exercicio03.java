import java.util.Scanner;

public class Exercicio03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();


        for (int contador = 0; contador < numero;contador++) {
            double questaoA = sc.nextDouble();
            double questaoB = sc.nextDouble();
            double questaoC = sc.nextDouble();

            double media = (questaoA * 2.0 + questaoB * 3.0 + questaoC * 5.0)/10.0;

            System.out.printf("%.1f%n",media);
        }
        sc.close();

    }

}

