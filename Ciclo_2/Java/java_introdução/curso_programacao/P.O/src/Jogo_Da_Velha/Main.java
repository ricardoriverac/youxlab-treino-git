package Jogo_Da_Velha;

import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("numeros.txt"));
        int maior = Integer.MIN_VALUE;

        String linha;
        while ((linha = br.readLine()) != null) {
            int num = Integer.parseInt(linha);
            if (num > maior) {
                maior = num;
            }
        }

        br.close();
        System.out.println("Maior número: " + maior);
    }
}
