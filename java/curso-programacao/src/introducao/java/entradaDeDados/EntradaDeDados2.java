package introducao.java.entradaDeDados;

import java.util.Scanner;

public class EntradaDeDados2 {
    public static void main(String[] args) {
        // Ler varios elementos até quebrar linha
        Scanner sc = new Scanner(System.in);
        // OBS: se colocamos um valor de tipo primitivo como int , double ect... , devemos colocar um proximo netxline vazio
        String s1 , s2 , s3;
        s1 = sc.nextLine();
        s2 = sc.nextLine();
        s3 = sc.nextLine();
        System.out.println("Dados guardados: ");
        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
        sc.close();
    }
}
