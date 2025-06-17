package java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.aplication;

import java_introdução.curso_programacao.P.O.src.src.ProblemaExemplo.entities.exVect_Ent;

import java.util.Locale;
import java.util.Scanner;

public class exVect_App {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);


        System.out.println("What are the numbers you will type?");
        int number = input.nextInt();
        exVect_Ent[] vect = new exVect_Ent[number];


        for (int i = 0; i < number; i++){
            System.out.println("Enter the number:");
            int numbers = input.nextInt();
            vect[i] = new exVect_Ent(numbers);
        }

        System.out.println("Negative numbers: ");

        for (exVect_Ent numerosNaLista : vect) {
            if (numerosNaLista.getNumbers() < 0) {
                System.out.println(numerosNaLista.getNumbers());
            }
            ;
        }


    }
}
