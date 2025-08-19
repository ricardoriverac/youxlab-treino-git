package execucao;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {

        File arquivo = new File("/home/youx/youxlab-treino-git/Java_estudo/aula155LendoArquivoTexto/in.txt");
        Scanner sc = null;

        try {
            sc = new Scanner(arquivo);
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.out.println("Erro: Arquivo não encontrado. Verifique o caminho.");
        } finally {
            if (sc != null) {
                sc.close();
            }
        }
    }
}
