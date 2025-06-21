package introducao.poo.exercicios.aplicacao;

import introducao.poo.exercicios.entities.Estudante;

import java.util.Locale;
import java.util.Scanner;

public class aplicacaoEstudante {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Estudante estudante = new Estudante();
        System.out.println("-Entrada de aluno-");
        System.out.print("Nome: ");
        estudante.nome = sc.nextLine();
        System.out.print("Nota 1: ");
        estudante.nota1 = sc.nextDouble();
        System.out.print("Nota 2: ");
        estudante.nota2 = sc.nextDouble();
        System.out.print("Nota 3: ");
        estudante.nota3 = sc.nextDouble();

        System.out.println("Resultado Final: " + estudante.somadanotas());
        sc.close();
    }
}
