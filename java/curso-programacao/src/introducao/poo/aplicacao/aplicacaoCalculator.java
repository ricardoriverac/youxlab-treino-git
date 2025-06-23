package introducao.poo.aplicacao;

import introducao.poo.entities.Calculator;

import java.util.Locale;
import java.util.Scanner;

public class aplicacaoCalculator {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);


        double radius = sc.nextDouble();
        double c = Calculator.circuferencia(radius);
        double v = Calculator.volume(radius);

        System.out.println(c);
        System.out.println(v);
    }
}
