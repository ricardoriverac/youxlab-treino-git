package introducao.poo.date_time.instanciacao;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class aplicationdata_time {
    public static void main(String[] args) {
        DateTimeFormatter fmt1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        LocalDate d01 = LocalDate.now();
        LocalDateTime d02 = LocalDateTime.now();
        Instant d03 = Instant.now();
        //
        LocalDateTime d04 = LocalDateTime.parse("2025-06-12T01:30:26");
        LocalDate d05 = LocalDate.parse("2025-12-06");
        Instant d06 = Instant.parse("2025-06-12T12:00:44Z");
        Instant d07 = Instant.parse("2025-06-12T12:00:44-03:00");

        LocalDate d08 = LocalDate.parse("12/06/2022", fmt1);
        // Formatar de um jeito personalizado
        LocalDateTime d09 = LocalDateTime.parse("12/05/2022 13:00", DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
        LocalDate d10 = LocalDate.of(2020, 06, 11);
        LocalDateTime d11 = LocalDateTime.of(2004, 05, 12, 04, 15, 12, 00004);


        System.out.println("d01 = " + d01.toString());
        System.out.println("d02 = " + d02.toString());
        System.out.println("d03 = " + d03.toString());
        System.out.println("d04 = " + d04.toString());
        System.out.println("d05 = " + d05.toString());
        System.out.println("d06 = " + d06.toString());
        System.out.println("d07 = " + d07.toString());
        System.out.println("d08 = " + d08.toString());
        System.out.println("d09 = " + d09.toString());
        System.out.println("d10 = " + d10.toString());
        System.out.println("d11 = " + d11.toString());

    }
}
