import java.util.Locale;
import java.util.Scanner;

public class ExeCont {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
//        String produtc1 = "computer";
//        String produtc2 = "office desk";
//
//        int age = 30;
//        int code = 5290;
//        char gender = 'F';
//
//        double price1 = 2100.0;
//        double price2 = 650.50;
//        double measure = 53.2345;
//
//        System.out.println("Product:");
//        System.out.printf("%s, which price is %.2f %n" , produtc1 , price1);
//        System.out.printf("Record: %d years old, code %d and gender: %s %n" , age , code , gender);
//        System.out.printf("Measure with eight decimal places: %f %n",  measure );
//        System.out.printf("Rouded (three decimal places): %.2f" , measure);
//
//        // Entrada de Dados
          Scanner sc = new Scanner(System.in);
//
//        double x;
//        int y;
//        String z;
//        char k;
//       x = sc.nextDouble();
//        x = sc.nextInt();
//        y = sc.nextDouble();
//        k = sc.next().charAt(0);
//        z = sc.nextDouble();
//        System.out.println("Você digitou " + x);
//        sc.close();

        // Ler em varios dados em varias linhas
//
//        String x;
//        int y;
//        double z;
//        x = sc.next();
//        y = sc.nextInt();
//        z = sc.nextDouble();
//        System.out.println("Dados digitados");
//        System.out.println(x);
//        System.out.println(y);
//        System.out.println(z);

        // Lendo texto até uma quebra de linha
        String s1 , s2,  s3;
        s1 = sc.nextLine();
        s2 = sc.nextLine();
        s3 = sc.nextLine();
        System.out.println("Dados digitados");
        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
        sc.close();
    }
}
