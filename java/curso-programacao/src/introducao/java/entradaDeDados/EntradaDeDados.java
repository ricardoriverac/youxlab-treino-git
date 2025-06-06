package introducao.java.entradaDeDados;

import java.util.Locale;
import java.util.Scanner;

public class EntradaDeDados {
    /// Aprender a fazer entrada de dados
    public static void main(String[] args) {
        // Colocando para um objeto para pra ser um atribuito de entrada de dados
        Scanner sc =  new Scanner(System.in);

        char w;
        double x;
        int y;
        String z;

        // OBS: a ordem da declarão de variáveis tem ser a mesma na entrada de dados
        z = sc.next();
        w = sc.next().charAt(0);
        y = sc.nextInt();
        x = sc.nextDouble();
        Locale.setDefault(Locale.US);
        System.out.printf("Nome: %s Sexo: %s idade: %d salario: %.2f" , z , w , y , x);
        sc.close();



    }
}
