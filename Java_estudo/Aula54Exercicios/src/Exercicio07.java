import java.util.Scanner;

public class Exercicio07 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numero = sc.nextInt();
        for(int contador =10;contador <numero;contador++){

            int primeiro = contador;
            int segundo = contador * contador;
            int terceiro = contador * contador * contador;
            System.out.println(primeiro+segundo+terceiro);
        }
        sc.close();
    }
}
