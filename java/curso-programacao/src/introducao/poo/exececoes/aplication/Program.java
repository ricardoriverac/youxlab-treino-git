package introducao.poo.exececoes.aplication;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        try {
            String[] vect = input.nextLine().split(" ");
            int position = input.nextInt();
            System.out.println(vect[position]);
        } catch (ArrayIndexOutOfBoundsException error) {
            System.out.println("Indice inexistente");
        } catch (InputMismatchException inputError){
            System.out.println("Input error");
        }

        input.close();

    }
}
