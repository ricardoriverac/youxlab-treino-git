package execucao;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        metodo1();

        System.out.println("Termino de seu programa!!! ");
    }
    public static void metodo1(){
        System.out.println("INICIO DO MÉTODO 1");
        metodo2();
        System.out.println("FIM DO MÉTODO 2");
    }

    public static void metodo2(){
        System.out.println("FIM DO MÉTODO 2");
        Scanner sc = new Scanner(System.in);
        try {
            String[] vect = sc.nextLine().split(" ");

            int posicao = sc.nextInt();
            System.out.println(vect[posicao]);
        }
        catch (ArrayIndexOutOfBoundsException excecao){
            System.out.println("Posição inválida ");
            excecao.printStackTrace();
        }
        catch (InputMismatchException excecao){
            System.out.println("Erro no input");
        }
        sc.close();
        System.out.println("FIM DO MÉTODO 2");
    }
}

