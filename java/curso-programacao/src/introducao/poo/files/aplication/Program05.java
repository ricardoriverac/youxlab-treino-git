package introducao.poo.files.aplication;

import java.io.File;
import java.util.Scanner;

public class Program05 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Entre com o nome pasta");
        String strpath = input.nextLine();
        File path = new File(strpath);

        File[] pastas = path.listFiles(File::isDirectory);
        System.out.println("Pastas: ");
        for (File pasta : pastas) {
            System.out.println(pasta);
        }

        File[] arquivos = path.listFiles(File::isFile);
        System.out.println("FILES: ");
        for (File arquivo : arquivos) {
            System.out.println(arquivo);
        }

        // Criando subpastas
        boolean sucesso = new File(strpath + "//subdir").mkdir();
        System.out.println("criado" + sucesso);
        input.close();
    }
}
