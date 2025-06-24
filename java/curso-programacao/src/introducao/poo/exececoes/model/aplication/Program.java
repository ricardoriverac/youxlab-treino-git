package introducao.poo.exececoes.model.aplication;

import introducao.poo.exececoes.model.entities.DomainException;
import introducao.poo.exececoes.model.entities.Reservation;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Program {
    public static void main(String[] args)  {
        Scanner input = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        try {

            System.out.print("Room number: ");
            int number = input.nextInt();
            System.out.print("Check-in Date (dd/MM/yyyy) ");
            Date checkin = sdf.parse(input.next());
            System.out.print("Check-out Date (dd/MM/yyyy) ");
            Date checkout = sdf.parse(input.next());
            Reservation reservation = new Reservation(number, checkin, checkout);
            System.out.println(reservation);

            System.out.println();
            System.out.println("Enter the date to uptade the reservation");
            System.out.print("Check-in Date (dd/MM/yyyy) ");
            Date checkIn = sdf.parse(input.next());
            System.out.print("Check-out Date (dd/MM/yyyy) ");
            Date checkOut = sdf.parse(input.next());
            System.out.println(reservation);

            reservation.updateDates(checkIn, checkOut);
            System.out.println(reservation);

            reservation.updateDates(checkIn, checkOut);
            System.out.println("Reservation: " + reservation);
        }
        catch (ParseException error){
            System.out.println("Invalid date format");
        }
        catch (DomainException errorArgs){
            System.out.println("Reservertion: " + errorArgs.getMessage());
        }
        input.close();
    }
}
