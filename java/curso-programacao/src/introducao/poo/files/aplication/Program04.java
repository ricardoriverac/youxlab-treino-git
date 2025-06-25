package introducao.poo.files.aplication;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Program04 {
    public static void main(String[] args) throws IOException {
        String[] lines = new String[] {"Good morning " , "Boa tarde" , "Boa noite"};

        String path = "/home/youx/workspace-git/youxlab-treino-git/java/curso-programacao/src/introducao/poo/files/out.txt";
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path , true))){
            for (String line : lines) {
                bw.write(line);
                bw.newLine();
            }
        }catch (IOException errorFile){
            errorFile.printStackTrace();
        }

    }
}
