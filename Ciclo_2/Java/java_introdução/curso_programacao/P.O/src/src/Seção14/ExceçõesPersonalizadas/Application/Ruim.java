package Seção14.ExceçõesPersonalizadas.Application;

import Seção14.ExceçõesPersonalizadas.Entities.ReservationR;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Ruim {
    public static void main(String[] args) throws ParseException {

        Scanner input = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");


        System.out.println("Room Number: ");
        int number = input.nextInt();
        System.out.println("Chek-int date (dd/MM/yyyy): ");
        Date chekIn = sdf.parse(input.next());

        System.out.println("Chek-Out date (dd/MM/yyyy): ");
        Date chekOut = sdf.parse(input.next());

        if(!chekOut.after(chekIn)){
            System.out.println("Error in reservation: Check-out date must be after check-in date");
        }
        else {
            ReservationR ReservationR = new ReservationR(number, chekIn, chekOut);
            System.out.println("Reservation: " + ReservationR);

            System.out.println();
            System.out.println("Enter data to update the reservation: ");
            System.out.println("Chek-int date (dd/MM/yyyy): ");
            chekIn = sdf.parse(input.next());
            System.out.println("Chek-Out date (dd/MM/yyyy): ");
            chekOut = sdf.parse(input.next());

            String error = ReservationR.updatesDates(chekIn, chekOut);
            if (error != null){
                System.out.println("Error in reservation: " + error);
            } else {
                System.out.println("Reservation: " + ReservationR);
            }
        }
        input.close();
    }
}
