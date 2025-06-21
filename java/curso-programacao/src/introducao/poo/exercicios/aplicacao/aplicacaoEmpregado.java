package introducao.poo.exercicios.aplicacao;

import introducao.poo.exercicios.entities.Empregado;

import java.util.Locale;
import java.util.Scanner;

public class aplicacaoEmpregado {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.println("Entrada de Empregado");
        Empregado empregado = new Empregado();
        System.out.print("Nome: ");
        empregado.nome = sc.nextLine();
        System.out.print("Salário bruto: ");
        empregado.salario_bruto = sc.nextDouble();
        System.out.print("Imposto: ");
        empregado.imposto = sc.nextDouble();

        System.out.printf("Salario taxado: %.2f %n", empregado.Salariotaxado());
        System.out.println("-Aumentando o salário-");
        System.out.print("Porcetagem de aumento do salário");
        double aumento = sc.nextDouble();
        empregado.AumentandoSalario(aumento);
        System.out.print("Aumento do salário do " + empregado);

    }
}
