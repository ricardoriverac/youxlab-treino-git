package atividadespraticas;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class atividadepratica03 {
    public static void main(String[] args) {
        BufferedReader dadEnt = new BufferedReader(new InputStreamReader(System.in));
        int n1 = 0;
        int n2 = 0;
        int n3 = 0;
        System.out.println("fale a primeira nota: ");
        try {
            n1 = Integer.parseInt(dadEnt.readLine());
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        System.out.println("fale a segunda nota: ");
        try {
            n2 = Integer.parseInt(dadEnt.readLine());
        } catch (IOException ex) {
            ex.printStackTrace();
        }


        System.out.println("fale a terceira nota: ");
        try {
            n3 = Integer.parseInt(dadEnt.readLine());
        } catch (IOException ex) {
            ex.printStackTrace();
        }


        double soma = (n1 + n2 + n3) / 3;

        System.out.println("A média do aluno foi de : " + soma);
    }
}