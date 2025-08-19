package execucao;

import java.io.File;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Entre com uma pasta: ");
        String strCaminho = sc.nextLine();

        File caminho = new File(strCaminho);

        File[] pastas = caminho.listFiles(File::isDirectory);
        System.out.println("Pastas: ");
        for (File pasta : pastas){
            System.out.println(pasta);
        }

        File [] files = caminho.listFiles(File::isFile);
        System.out.println("Pastas: ");

        for (File pasta : pastas){
            System.out.println(pasta);

        }
        boolean sucesso = new File(strCaminho + "//subPasta").mkdir();
        System.out.println("Diretório criado com sucesso: " + sucesso);
        sc.close();
    }
}
