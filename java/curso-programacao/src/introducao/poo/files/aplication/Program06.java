package introducao.poo.files.aplication;

import java.io.File;
import java.util.Scanner;

public class Program06 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a file path: ");
        String strpath = input.nextLine();
        File file = new File(strpath);

        System.out.println("getName " + file.getName());
        System.out.println("getParent " + file.getParent());
        System.out.println("getPath/ " + file.getPath());
    }
}
