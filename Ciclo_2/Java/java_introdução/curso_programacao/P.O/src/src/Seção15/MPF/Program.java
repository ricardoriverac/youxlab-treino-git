package Seção15.MPF;

import java.io.File;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {

        // Cria o objeto Scanner para ler entrada do usuário
        Scanner sc = new Scanner(System.in);

        // Pede ao usuário que digite o caminho da pasta
        System.out.println("Enter a folder path: ");
        String strPath = sc.nextLine(); // Lê o caminho digitado

        // Cria um objeto File com base no caminho informado
        File path = new File(strPath);

        // Lista os diretórios (pastas) dentro do caminho informado
        File[] folders = path.listFiles(File::isDirectory);
        System.out.println("FOLDERS");
        for (File folder : folders){
            System.out.println(folder); // Imprime o caminho de cada pasta
        }

        // Lista os arquivos dentro do caminho informado
        File[] files = path.listFiles(File::isFile);
        for (File file : files){
            System.out.println(file); // Imprime o caminho de cada arquivo
        }

        // Cria uma nova subpasta chamada "subdir" dentro da pasta fornecida
        boolean sucess = new File(strPath + "\\subdir").mkdir();
        System.out.println("Diretorio criado com sucesso: " + sucess);

        // Fecha o scanner
        sc.close();
    }
}
