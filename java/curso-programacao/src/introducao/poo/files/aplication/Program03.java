package introducao.poo.files.aplication;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Program03 {
    public static void main(String[] args) {
        String path  = "/home/youx/Downloads/in.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(path))){
            String line = br.readLine();
            while (line != null){
                System.out.println(line);
                line = br.readLine();
            }
        }catch (IOException errorFile){
            System.out.println("Error " + errorFile.getMessage());
        }
    }
}
