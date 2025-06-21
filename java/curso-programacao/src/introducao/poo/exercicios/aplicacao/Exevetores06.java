package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores06 {
    ///  <p style= color:purple>Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
    /// terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
    /// o vetor C gerado.<p/>
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Quantos valores vai ter cada vetor? ");
        int quant = input.nextInt();
        int[] arrayA = new int[quant];
        int[] arrayB = new int[quant];
        int[] arrayC = new int[quant];
        System.out.println("Digite os valores do vetor A: ");
        for (int i = 0; i < arrayA.length; i++) {
            arrayA[i] = input.nextInt();
        }
        System.out.println("Digite os valores do vetor B: ");
        for (int i = 0; i < arrayB.length ; i++) {
            arrayB[i] = input.nextInt();
        }
        System.out.println("Resultante");
        for (int i = 0; i < arrayC.length; i++) {
            arrayC[i] = arrayA[i] += arrayB[i];
            System.out.println(arrayC[i]);
        }


        input.close();
    }
}
