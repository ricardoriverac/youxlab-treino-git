package introducao.poo.date_time.instanciacao;


import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;

public class operacoesData_Hora {
    public static void main(String[] args) {
        LocalDate d01 = LocalDate.parse("2020-04-22");
        LocalDate d02 = LocalDate.parse("2020-04-22");
        Instant d03 = Instant.parse("2020-04-22T01:00:00Z");

        LocalDate r1 = LocalDate.ofInstant(d03 , ZoneId.of("Europe/Monaco"));
        LocalDate r2 = LocalDate.ofInstant(d03 , ZoneId.systemDefault());
        LocalDate r3 = LocalDate.ofInstant(d03 , ZoneId.of("Portugal"));
        LocalDateTime r4 = LocalDateTime.ofInstant(d03 , ZoneId.of("Portugal"));

        System.out.println("Horario de monaco " + r1);
        System.out.println("Horario de são paulo " + r2);
        System.out.println("Horario de portugal " +  r3);
        System.out.println("Data e hora de portugal " + r4);

        // Obter dados de datahora local e global


        // Pegando o dia do mes
        System.out.println("do1 dia = " + d01.getDayOfMonth());
        // Pega o nome do mes
        System.out.println("do1 mes = " + d01.getMonth());
        // Pega o valor do mes
        System.out.println("do1 mes = " + d01.getMonthValue());
        // Ano
        System.out.println("d02 hora = " + d02.atStartOfDay().withHour(2));
        System.out.println("d02 hora = " + d02.atStartOfDay().getMinute());



    }
}
