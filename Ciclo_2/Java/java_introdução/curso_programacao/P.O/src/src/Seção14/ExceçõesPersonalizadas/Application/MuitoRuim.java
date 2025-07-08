package Seção14.ExceçõesPersonalizadas.Application;

import Seção14.ExceçõesPersonalizadas.Entities.ReservationMR;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class MuitoRuim {
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
            ReservationMR reservationMR = new ReservationMR(number, chekIn, chekOut);
            System.out.println("Reservation: " + reservationMR);

            System.out.println();
            System.out.println("Enter data to update the reservation: ");
            System.out.println("Chek-int date (dd/MM/yyyy): ");
            chekIn = sdf.parse(input.next());
            System.out.println("Chek-Out date (dd/MM/yyyy): ");
            chekOut = sdf.parse(input.next());

            Date now = new Date();
            if (chekIn.before(now) || chekOut.before(now)){
                System.out.println("Error in reservation: Reservation dates for update must be future");
            } else if (!chekOut.after(chekIn)) {
                System.out.println("Error in reservation: Check-out date must be after check-in date");
            } else {
                reservationMR.updatesDates(chekIn, chekOut);
                System.out.println("Reservation: " + reservationMR);
            }
        }
        input.close();
    }
}
