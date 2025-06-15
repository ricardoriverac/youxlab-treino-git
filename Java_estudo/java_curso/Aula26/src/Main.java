import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        //int x;
        //x = sc.nextInt();
        //System.out.println("Você fez seu primeiro 'imput' no java: "+ x);

        //sc.close();
        Locale.setDefault(Locale.US);
        //double x;
        //x = sc.nextDouble();
        //System.out.printf("Voce digitou: %.2f%n",x);

        //char x;
        //x = sc.next().charAt(0);
        //System.out.println("Você digitou "+ x);

        //sc.close();

        String x;
        int y;
        double z;
        x = sc.next();
        y = sc.nextInt();
        z = sc.nextDouble();
        System.out.println("Dados digitados: ");
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);









    }
}

