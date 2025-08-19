package aplicacao;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class Programa {
    public static void main(String[] args) {
        //https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/format/DateTimeFormatter.html

        DateTimeFormatter formato1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        DateTimeFormatter formato2 = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

        LocalDate d01 = LocalDate.now();
        LocalDateTime d02 = LocalDateTime.now();
        Instant d03 = Instant.now();
        LocalDate d04 = LocalDate.parse("2025-01-19");
        LocalDateTime d05 = LocalDateTime.parse("2025-01-19T01:30:26");
        Instant d06 = Instant.parse("2025-01-19T01:30:26Z");
        Instant d07 = Instant.parse("2025-01-19T01:30:26-03:00");
        LocalDate d08 = LocalDate.parse("20/07/2022",formato1);
        LocalDateTime d09 = LocalDateTime.parse("20/07/2022 14:30",formato2);
        LocalDate d10 = LocalDate.of(2022,7,20);
        LocalDateTime d11 = LocalDateTime.of(2022,3,5,3,5,30,2);

        System.out.println(d03);
        System.out.println(d01);
        System.out.println(d02);
        System.out.println(d04);
        System.out.println(d05);
        System.out.println(d06);
        System.out.println(d07);
        System.out.println(d08);
        System.out.println(d09);
        System.out.println(d10);
        System.out.println(d11);
    }
}
