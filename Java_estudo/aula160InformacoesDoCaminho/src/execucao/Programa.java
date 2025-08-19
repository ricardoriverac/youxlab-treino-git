package execucao;

import java.io.File;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Entre com o caminho do arquivo: ");
        String strCaminho = sc.nextLine();

        File caminho = new File(strCaminho);

        System.out.println("getName: " + caminho.getName());
        System.out.println("getParent: " + caminho.getParent());//Só o caminho sem nome
        System.out.println("getPath: " + caminho.getPath());

        sc.close();
    }
}
