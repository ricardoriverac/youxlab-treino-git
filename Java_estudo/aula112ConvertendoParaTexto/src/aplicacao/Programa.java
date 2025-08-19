package aplicacao;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

public class Programa {
    public static void main(String[] args) {
        LocalDate d04 = LocalDate.parse("2025-01-19");
        LocalDateTime d05 = LocalDateTime.parse("2025-01-19T01:30:26");
        Instant d06 = Instant.parse("2025-01-19T01:30:26Z");

        DateTimeFormatter formato1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        DateTimeFormatter formato3 = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm").withZone(ZoneId.systemDefault());




        System.out.println("d04 = "+ d04.format(formato1));
        System.out.println("d04 = " + formato1.format(d04));
        System.out.println("d04 = " + d04.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));
        System.out.println("d06 = " + formato3.format(d06));

    }
}
