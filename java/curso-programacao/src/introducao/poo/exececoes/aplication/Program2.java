package introducao.poo.exececoes.aplication;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Program2 {
    public static void main(String[] args) {
        method1();
    }

    public static void method1(){
        System.out.println("**Method 1 enter**");
        method2();
        System.out.println("**Method 1 final**");
    }
    public static void method2(){
        System.out.println("Method 2");
    Scanner input = new Scanner(System.in);
        try {
        String[] vect = input.nextLine().split(" ");
        int position = input.nextInt();
        System.out.println(vect[position]);
    } catch (ArrayIndexOutOfBoundsException error) {
        System.out.println("Indice inexistente");
        // Mostrar erros em colunas de métodos
        error.printStackTrace();
        input.nextInt();
    } catch (
    InputMismatchException inputError){
        System.out.println("Input error");

    }
        System.out.println("**Final method 2");
    }
}
