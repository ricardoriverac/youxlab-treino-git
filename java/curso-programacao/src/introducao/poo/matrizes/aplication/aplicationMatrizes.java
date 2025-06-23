package introducao.poo.matrizes.aplication;

import java.util.Scanner;

public class aplicationMatrizes {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int quant = input.nextInt();
        int[][] mat = new int[quant][quant];
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                mat[i][j] = input.nextInt();
            }
        }
        System.out.println("Diagonal principal");
        for (int i = 0; i < mat.length; i++) {
            System.out.print(mat[i][i] + " ");
        }
        System.out.println();
        int count = 0;
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] < 0){
                    count++;
                }
            }

        }
        System.out.println("Quantidade de números negativos: " + count);
        System.out.println("Variáveis da array multidimensional");
        for (int[] arraybase : mat){
            for (int arrayp : arraybase){
                System.out.println(arrayp);
            }
        }
    }
}
