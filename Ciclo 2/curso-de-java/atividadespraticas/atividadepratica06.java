package atividadespraticas;

import java.util.Arrays;
import java.util.Scanner;
public class atividadepratica06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] guardar = new int[10];
        for (int i = 0; i < 10; i++) {
            int n1 = sc.nextInt();
            guardar[i] = n1;
        }

        int [] [] n1 = new int[10] [10];

        System.out.println(Arrays.toString(guardar));


    }
}
