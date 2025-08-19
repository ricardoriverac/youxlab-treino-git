package execucao;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Programa {
    public static void main(String[] args) {
        String caminho = "/home/youx/youxlab-treino-git/Java_estudo/aula155LendoArquivoTexto/in.txt";

        try (BufferedReader br = new BufferedReader(new FileReader(caminho))){

            String linha = br.readLine();

            while (linha != null) {
                System.out.println(linha);
                linha = br.readLine();
            }
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }

    }
}

