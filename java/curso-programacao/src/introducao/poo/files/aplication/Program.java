package introducao.poo.files.aplication;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        File file = new File("/home/youx/Downloads/in.txt");
        Scanner input = null;
        try {
            input = new Scanner(file);
            while (input.hasNextLine()){
                System.out.println(input.nextLine());
            }
        }catch (IOException errorFile){
            System.out.println("Error" + errorFile.getMessage());
        }
        finally {
            if (input != null) {
                input.close();
            }
        }
    }
}
