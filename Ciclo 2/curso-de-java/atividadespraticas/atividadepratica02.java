package atividadespraticas;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class atividadepratica02 {
    public static void main(String[] args) {
        BufferedReader dadEnt = new BufferedReader(new InputStreamReader(System.in));
        int n1 = 0;
        System.out.println("Solicite um número de 0 a 10: ");
        try {
            n1 = Integer.parseInt(dadEnt.readLine());
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        ;
        if (n1 <= 10) {
            System.out.println("número correto.");
        }
        else {
                System.out.println("número inválido.");
            }
         ;
    }
}