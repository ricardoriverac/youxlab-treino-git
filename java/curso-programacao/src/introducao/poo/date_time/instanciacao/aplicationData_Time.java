package introducao.poo.date_time.instanciacao;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

public class aplicationData_Time {
    public static void main(String[] args) {
        // Formatação
        LocalDateTime d01 = LocalDateTime.parse("2020-04-12T14:00");
        LocalDate d02 = LocalDate.parse("2020-03-12");
        // Data Global e o instant
        Instant d03 = Instant.parse("2020-03-20T14:00:44Z");

        DateTimeFormatter fm1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        DateTimeFormatter fm2 = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm").withZone(ZoneId.systemDefault());
        DateTimeFormatter fm3 = DateTimeFormatter.ISO_DATE_TIME;
        DateTimeFormatter fm4 = DateTimeFormatter.ISO_INSTANT;

        LocalDateTime teste = LocalDateTime.now();


        System.out.println("d01 = " + d01.format(fm1));
        System.out.println("d01 = " + fm1.format(d01));

        System.out.println("d02 = " + d02.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));
        System.out.println("d01 = " + fm1.format(d01));
        System.out.println("d03 = " + fm2.format(d03));
        System.out.println("d01 = " + fm3.format(d01));
        System.out.println("d03 = " + fm4.format(d03));
        System.out.println("teste = " + teste);





    }
}
