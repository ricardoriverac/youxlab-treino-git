package Seção14.BlocoFinally;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        File file = new File("C:\\temp\\in.text");
        Scanner input = null;

        try {
            input = new Scanner(file);
            while (input.hasNextLine()) {
            }
            System.out.println(input.nextLine());

        } catch (FileNotFoundException e) {
            System.out.println("Error open file: " + e.getMessage());
        } finally {
            if (input != null) {
                input.close();
            }
        }
    }
}