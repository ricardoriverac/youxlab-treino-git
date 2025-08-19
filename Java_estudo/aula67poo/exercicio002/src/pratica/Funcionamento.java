package pratica;

import entidade.Funcionario;

import java.util.Locale;
import java.util.Scanner;

public class Funcionamento {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Funcionario funcionario = new Funcionario();
        System.out.print("Nos diga o nome do funcionário: ");
        funcionario.nome = sc.nextLine();

        System.out.print("Seu salário e: ");
        funcionario.salario = sc.nextInt();

        System.out.print("O salário menos os impostos ");
        funcionario.imposto = sc.nextInt();

        System.out.println(funcionario.salarioDescontado());

    }
}
