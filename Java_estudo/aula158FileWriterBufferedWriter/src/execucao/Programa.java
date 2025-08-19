package execucao;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Programa {
    public static void main(String[] args) {
        String [] lines = new String[]{"Bom dia ","Boa tarde ","Boa noite "};

        String escolha = "/home/youx/youxlab-treino-git/Java_estudo/aula158FileWriterBufferedWriter/in.txt";

        try (BufferedWriter bw = new BufferedWriter(new FileWriter(escolha,true))){
            for (String linha : lines){
                bw.write(linha);
                bw.newLine();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
