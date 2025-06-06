package introducao.java.exercicios.Sequencial;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio4 {
    /// Fazer um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por
    /// hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas
    /// decimais.
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int numero_funcionario = sc.nextInt();
        int horas = sc.nextInt();
        double valorRecebe = sc.nextDouble();

        double salario = horas * valorRecebe;

        System.out.println("Número do funcionario: " + numero_funcionario);
        System.out.printf("Salário do funcionario: U$ %.2f" , salario);

    }
}
