package exercicios_Vetor;

import java.util.Locale;
import java.util.Scanner;
 public class exercicio04 {
     public static void main(String[] args) {

         Locale.setDefault(Locale.US);
         Scanner sc = new Scanner(System.in);

         int n;
         n = sc.nextInt();

         int[] pares = new int[n];
         for (int i = 0; i < n; i++) {
             pares[i] = sc.nextInt();
             if (pares[i] % 2 == 0) {
                 System.out.printf("%d  ", pares[i]);
                 }
             }
         }
     }

