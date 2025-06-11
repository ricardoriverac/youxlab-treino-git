package java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.aplication;

import java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.entities.ex3_entities;

import java.util.Locale;
import java.util.Scanner;

public class ex3_aplication {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        ex3_entities ent = new ex3_entities();

        System.out.print("Opa qual seu nome?: ");
        String nome = input.nextLine();
        System.out.println();

        System.out.println("Quais foram suas notas nesses 3 trimestres?: ");
        ent.nota1 = input.nextDouble();
        ent.nota2 = input.nextDouble();
        ent.nota3 = input.nextDouble();

        System.out.printf("FINAL GRADE: %.2f%n", ent.somaDasnota());
        if (ent.somaDasnota() < 60.0) {
            System.out.println("FAILED");
            System.out.printf("MISSING %.2f POINTS%n", ent.quantosPontosFalta());
        }
        else {
            System.out.println("PASS");
        }
        input.close();
    }
}