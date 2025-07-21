package ProblemaExemplo.aplication;

import ProblemaExemplo.entities.ExNegativeEnt;

import java.util.Locale;
import java.util.Scanner;

public class ExNegativesVect {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);


        System.out.println("What are the numbers you will type?");
        int number = input.nextInt();
        ExNegativeEnt[] vect = new ExNegativeEnt[number];


        for (int i = 0; i < number; i++){
            System.out.println("Enter the number:");
            int numbers = input.nextInt();
            vect[i] = new ExNegativeEnt(numbers);
        }

        System.out.println("Negative numbers: ");

        for (ExNegativeEnt numerosNaLista : vect) {
            if (numerosNaLista.getNumbers() < 0) {
                System.out.println(numerosNaLista.getNumbers());
            }
            ;
        }


    }
}
