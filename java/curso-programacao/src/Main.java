import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        System.out.print("Olá Mundo ");
        System.out.println("Bom dia!");

        int y = 32;
        double x = 10.93929;
        System.out.println(y);
        System.out.println(x);
        System.out.printf("%.2f%n" , x);
        System.out.printf("%.4f%n" , x);
        System.out.printf("%.4f%n" , x);
        // Mudar o idioma
        Locale.setDefault(Locale.US);
        // Concatenar os resultados
        System.out.println("Resuldado = " + x + " Metros");
        System.out.printf("Resultado %.2f metros%n" , x);

        // concater elementos de em um mesmo comando em escrita
        String nome = "Maria";
        int idade = 31;
        double renda = 4000.0;
        /*
        %s Tipo para concatenar strings
        %d numeros
        %f formatar números
         */

        System.out.printf("%s tem %d anos e ganha %.2f reais %n" , nome,  idade , renda);

    }
}
