package java_introdução.curso_programacao;

import javax.xml.transform.Source;
import java.util.Scanner;

public class ex1_for {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int x;

        x = input.nextInt();

        for (int i = 1; i <= x; i++) {
            if (i % 2 != 0) {
                System.out.println(i);
            }


        }
    }
}