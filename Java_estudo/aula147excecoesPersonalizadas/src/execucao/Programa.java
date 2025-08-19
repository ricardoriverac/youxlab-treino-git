package execucao;

import entidade.Reserva;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args)throws ParseException {
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        System.out.println("Número do quarto: ");
        int numero = sc.nextInt();

        System.out.println("Check-in date (dd/MM/yyyy): ");
        Date checkIn = sdf.parse(sc.next());

        System.out.println("Check-out date (dd/MM/yyyy): ");
        Date checkOut = sdf.parse(sc.next());

        if (!checkOut.after(checkIn)){
            System.out.println("Erro em reserva: check-out está com uma data além do checkIn ");
        }
        else {
            Reserva reserva = new Reserva(numero,checkIn,checkOut);
            System.out.println("Reserva:: " + reserva);

            System.out.println();

            System.out.println("Entre com as datas atualizadas: ");
            System.out.println("Check-in date (dd/MM/yyyy): ");
            checkIn = sdf.parse(sc.next());

            System.out.println("Check-out date (dd/MM/yyyy): ");
            checkOut = sdf.parse(sc.next());

            Date now = new Date();
            if (checkIn.before(now)|| checkOut.before(now) ){
                System.out.println("Erro na reserva as reservas devem ser repassadas em datas fúturas ");
            }
            else if(!checkOut.after(checkIn)){
                System.out.println("Erro em reserva: check-out está com uma data além do checkIn");
                System.out.println("Reserva: "+ reserva);
            }
            else {
                reserva.updateDates(checkIn, checkOut);
                System.out.println("Reserva:: " + reserva);
            }


        }


        sc.close();



    }
}
