package introducao.java.estruturaCondicional;

import java.util.Scanner;

public class EstruturaEncadeada {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Quantas horas?");
        int horas = sc.nextInt();

        if (horas <= 12){
            System.out.println("Bom dia");
        }
        else if (horas < 18) {
            System.out.println("Boa tarde");
        }
        else {
            System.out.println("Boa noite");
        }
    }
}
