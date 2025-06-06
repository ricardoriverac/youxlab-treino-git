package introducao.java.estruturaCondicional;

import java.util.Scanner;

public class EstruturaComposta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Quantas horas?");
        int horas = sc.nextInt();

        if (horas < 18) {
            System.out.println("Boa tarde");
        }
        else {
            System.out.println("Boa noite");
        }
    }
}
