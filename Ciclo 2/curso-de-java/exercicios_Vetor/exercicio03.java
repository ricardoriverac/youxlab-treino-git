package exercicios_Vetor;

import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class exercicio03 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int n;
        n = sc.nextInt();

        String[] nomes = new String[n];
        int[] idades = new int[n];
        double[] alturas = new double[n];
        for (int i = 0; i < n; i++) {
            nomes[i] = sc.next();
            idades[i] = sc.nextInt();
            alturas[i] = sc.nextDouble();
            System.out.println(Arrays.toString(nomes));
            System.out.println(Arrays.toString(idades));
            System.out.println(Arrays.toString(alturas));
        }
    }
}