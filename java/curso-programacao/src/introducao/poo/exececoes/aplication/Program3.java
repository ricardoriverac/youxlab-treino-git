package introducao.poo.exececoes.aplication;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Program3 {
    public static void main(String[] args) {
        File file = new File("/home/youx/Downloads/in.txt");
        Scanner sc = null;
        try {
            sc = new Scanner(file);
            while (sc.hasNextLine()){
                System.out.println(sc.nextLine());
            }
        }catch (FileNotFoundException errorFile){
            System.out.println("Error ao abrir o arquivo " + errorFile.getMessage());
        } finally {
            if (sc != null){
                sc.close();
            }
            System.out.println("Fechando o arquivo");
        }
   }
}
