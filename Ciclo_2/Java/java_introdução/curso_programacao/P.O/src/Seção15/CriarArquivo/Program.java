package Seção15.CriarArquivo;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Program {
    public static void main(String[] args) {

        String[] lines = new String[] { "Bom dia", "Boa Tarde", "Boa Noite"};

        String path = "/home/youxlab/Documentos/in.txt";

        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path))){
            for (String line : lines){
                bw.write(line);
                bw.newLine();
            }
        }

        catch (IOException e){
            e.printStackTrace();
        }
    }
}
