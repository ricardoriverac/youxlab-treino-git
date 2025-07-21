package ProblemaExemplo.aplication;

import ProblemaExemplo.ultil.aula71_ultil;

import java.util.Locale;
import java.util.Scanner;

public class aula71_2 {
    public static void main(String[] args) {
        aula71_ultil cal = new aula71_ultil();
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);


        System.out.print("Enter radius: ");
        double radius = input.nextDouble();

        double c = cal.circumference(radius);
        double v = cal.volume(radius);

        System.out.printf("Circumference: %.2f%n", c);
        System.out.printf("Volume: %.2f%n", v);
        System.out.printf("PI value: %.2f%n", cal.PI);

    }
}
