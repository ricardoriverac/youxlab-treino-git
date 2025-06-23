package introducao.poo.exececoes.model.aplication;

import introducao.poo.exececoes.model.entities.Reservation;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) throws ParseException {
        Scanner input = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        System.out.print("Room number: ");
        int number = input.nextInt();
        System.out.print("Check-in Date (dd/MM/yyyy) ");
        Date checkin = sdf.parse(input.next());
        System.out.print("Check-out Date (dd/MM/yyyy) ");
        Date checkout = sdf.parse(input.next());
        if (!checkout.after(checkin)) {
            System.out.println("Error in reservation: check-out must be after check-in date");
        } else {
            Reservation reservation = new Reservation(number, checkin, checkout);
            System.out.println(reservation);

            System.out.println();
            System.out.println("Enter the date to uptade the reservation");
            System.out.print("Check-in Date (dd/MM/yyyy) ");
            Date checkIn = sdf.parse(input.next());
            System.out.print("Check-out Date (dd/MM/yyyy) ");
            Date checkOut = sdf.parse(input.next());
            System.out.println(reservation);

            reservation.updateDates(checkIn , checkOut);
            System.out.println(reservation);

            Date now = new Date();
            if  (checkIn.before(now) || checkOut.before(now)){
                System.out.println("Error in reservation: Reservation dates for update must be future dates");
            } else if (!checkOut.after(checkIn)){
                System.out.println("Error in reservation: Check-out date must be after ckeck-in date");
            } else{
                reservation.updateDates(checkIn , checkOut);
                System.out.println("Reservation: " + reservation);
            }
        }
        input.close();
    }
}
