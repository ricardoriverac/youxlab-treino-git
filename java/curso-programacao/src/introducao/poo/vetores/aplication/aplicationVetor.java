package introducao.poo.vetores.aplication;

import java.util.Locale;
import java.util.Scanner;

public class aplicationVetor {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        int inicio = input.nextInt();
        double [] vect = new double[inicio];
        double soma =  0.0;
        for (int i = 0;  i<inicio ; i++) {
            vect[i] = input.nextDouble();
            soma += vect[i];
        }
        double avg = soma / vect.length;
        System.out.println(avg);
    }
}
