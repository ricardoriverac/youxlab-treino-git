import java.util.Locale;

public class Main {
    public static void main(String[]args){
        double x = 10.323;
        String nome = "Maria";
        int idade = 31;
        double renda =4000.0;

        System.out.printf("%.2f%n",x);

        System.out.println("Olá mundo");

        System.out.println("O começo do fim");

        Locale.setDefault(Locale.US);

        System.out.printf("%.2f%n",x);

        System.out.println("Resultado = " + x + " Metros");

        System.out.println("Resultado = %");

        System.out.printf("Resultado = %.2f metros%n",x);

        System.out.printf("%s tem %d anos e ganha R$ %.2f reais%n",nome,idade,renda);
    }
}

