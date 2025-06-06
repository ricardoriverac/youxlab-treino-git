package introducao.java;

import java.util.Locale;
import java.util.Scanner;

public class DebugnoIJ {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int difirenca = (a * b - c * d);
        System.out.printf("Diferença: %d" , difirenca);
        sc.close();
    }
}
