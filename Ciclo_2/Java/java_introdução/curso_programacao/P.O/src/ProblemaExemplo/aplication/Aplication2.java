package ProblemaExemplo.aplication;

import java.util.Locale;
import java.util.Scanner;

public class Aplication2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);


        System.out.println("What are the numbers you will type?");
        int number = input.nextInt();
        int[] vect = new int[number];

        for (int i = 0; i < number; i++) {
            System.out.print("Enter the number: ");
            int numbers = input.nextInt();
            vect[i] = numbers;
        }

        System.out.print("\nEven numbers: ");
        int count = 0;

        for (int value : vect) {
            if (value % 2 == 0) {
                System.out.println(value);
                count++;
            }
        }

        System.out.println("Quantity of even numbers: " + count);

        input.close();
    }
}
