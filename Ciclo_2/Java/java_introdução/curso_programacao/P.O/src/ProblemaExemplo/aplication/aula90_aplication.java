package ProblemaExemplo.aplication;

import ProblemaExemplo.entities.aula90_entities;

import java.util.Locale;
import java.util.Scanner;

public class aula90_aplication {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        aula90_entities[] vect = new aula90_entities[n];

        for (int i=0; i < vect.length; i++){
            input.nextLine();
            System.out.println("Name of product");
            String name = input.nextLine();

            System.out.println("Whath the price of product?");
            double price = input.nextDouble();
            vect[i] = new aula90_entities(name, price);
        }

        double sum = 0.0;
        for (int i=0; i< vect.length ; i++)
        {
            sum += vect[i].getPrice();
        }

        double avg = sum / vect.length;

        System.out.printf("AVAREGE PRICE: %.2f%n", avg);



        input.close();
    }
}
