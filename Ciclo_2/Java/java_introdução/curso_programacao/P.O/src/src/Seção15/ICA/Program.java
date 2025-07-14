package Seção15.ICA;

import java.io.File;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a file path: ");
        String strPath = sc.nextLine();

        File path = new File(strPath);

        System.out.println("getName: " + path.getPath());
        System.out.println("getParent" + path.getParent());
        System.out.println("getName" + path.getName());

        sc.close();
    }
}
