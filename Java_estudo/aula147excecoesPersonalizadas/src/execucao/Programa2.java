package execucao;

import entidade.Reserva2;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Programa2 {
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
            Reserva2 reserva2 = new Reserva2(numero,checkIn,checkOut);
            System.out.println("Reserva:: " + reserva2);

            System.out.println();

            System.out.println("Entre com as datas atualizadas: ");
            System.out.println("Check-in date (dd/MM/yyyy): ");
            checkIn = sdf.parse(sc.next());

            System.out.println("Check-out date (dd/MM/yyyy): ");
            checkOut = sdf.parse(sc.next());

            String erro = reserva2.updateDates(checkIn,checkOut);
            if (erro != null){
                System.out.println("Erro em reserva: " + erro);
            }
            else {
                System.out.println("Reserva:: " + reserva2);

            }

        }


        sc.close();



    }
}
