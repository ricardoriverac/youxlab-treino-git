package application.student;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        String name = sc.nextLine();
        double g1 = sc.nextDouble();
        double g2 = sc.nextDouble();
        double g3 = sc.nextDouble();

        Student student = new Student(name, g1, g2, g3);

        System.out.printf("FINAL GRADE = %.2f%n", student.finalGrade());
        if (student.isPassed()) {
            System.out.println("PASS");
        } else {
            System.out.println("FAILED");
            System.out.printf("MISSING %.2f POINTS%n", student.missingPoints());
        }

        sc.close();
    }
}
