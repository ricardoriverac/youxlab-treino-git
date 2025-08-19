package execucao;

import entidade.Reserva3;
import model.exceptions.DominioException;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Programa3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        try {

            System.out.println("Número do quarto: ");
            int numero = sc.nextInt();
            System.out.println("Check-in date (dd/MM/yyyy): ");
            Date checkIn = sdf.parse(sc.next());
            System.out.println("Check-out date (dd/MM/yyyy): ");
            Date checkOut = sdf.parse(sc.next());

            Reserva3 reserva3 = new Reserva3(numero, checkIn, checkOut);
            System.out.println("Reserva:: " + reserva3);

            System.out.println("---------------------------------------");

            System.out.println("Entre com as datas atualizadas: ");

            System.out.println("Check-in date (dd/MM/yyyy): ");
            checkIn = sdf.parse(sc.next());
            System.out.println("Check-out date (dd/MM/yyyy): ");
            checkOut = sdf.parse(sc.next());

            reserva3.updateDates(checkIn, checkOut);
            System.out.println("Reserva: " + reserva3);
        } catch (ParseException excecao) {
            System.out.println("Data informada inválida ");

        } catch (IllegalArgumentException excecao) {
            System.out.println("Data atribuída inválida. " + excecao.getMessage());
        } catch (DominioException excecao) {
            throw new RuntimeException(excecao);
        }
        catch (RuntimeException excecao){
            System.out.println("Erro inesperado");
        }

        sc.close();

    }
}

