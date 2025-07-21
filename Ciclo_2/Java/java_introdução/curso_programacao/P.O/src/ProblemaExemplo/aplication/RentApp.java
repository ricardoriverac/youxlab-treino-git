package ProblemaExemplo.aplication;

import ProblemaExemplo.entities.rentEnt;

import java.util.Locale;
import java.util.Scanner;

public class RentApp {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        rentEnt[] Vect = new rentEnt[10];

        System.out.println("How many rooms will be reted?: ");
        int numero = input.nextInt();

        for (int i = 0; i < numero; i++){
            System.out.println();
            System.out.println("Rent #" + i + ":");
            System.out.println("Name: ");
            input.nextLine();
            String name = input.nextLine();
            System.out.println("Email: ");
            String email = input.next();
            System.out.println("Room: ");
            int room = input.nextInt();

            Vect[room] = new rentEnt(name, email);
        }

        System.out.println();
        System.out.println("Busy rooms: ");
        for (int i = 0; i < 10; i++){
            if (Vect[i] != null){
                System.out.println(i + ": " + Vect[i]);
            }
        }
        input.close();
    }
}
