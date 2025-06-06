package introducao.java.tiposprimitivos;

import java.util.Locale;
import java.util.Scanner;

public class operadoresdeatribuito {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int minuto;
        minuto = sc.nextInt();
        double conta = 50.00;
        if (minuto > 100){
            conta += (minuto - 100) * 2.0;
        }
        System.out.printf("Valor da conta e R$%.2f", conta);

    }
}
