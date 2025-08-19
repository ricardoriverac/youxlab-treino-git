package aplicacao;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;

public class Programa {
    public static void main(String[] args) {

        LocalDate d04 = LocalDate.parse("2025-01-19");
        LocalDateTime d05 = LocalDateTime.parse("2025-01-19T01:30:26");
        Instant d06 = Instant.parse("2025-01-19T01:30:26Z");

        LocalDate resultado1 = LocalDate.ofInstant(d06,ZoneId.systemDefault());
        LocalDate resultado2 = LocalDate.ofInstant(d06,ZoneId.of("Portugal"));

        System.out.println("Resultado1 = " + resultado1);
        System.out.println("Resultado2 = " + resultado2);

        System.out.println("d04 dia = " + d04.getDayOfMonth());
        System.out.println("d05 ano = " + d05.getYear());
        System.out.println("d05 = " + d05.getMinute());
    }
}
