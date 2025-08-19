package funcionamento;

import entidade.Aluno;

import java.util.Locale;
import java.util.Scanner;

public class Atividade {

    static void mythedo(String nome){
        System.out.println(nome);
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Aluno aluno = new Aluno();

        aluno.setBim1(sc.nextDouble());
        System.out.println("Bimestre 1: " + aluno.getBim1());

        aluno.setBim2(sc.nextDouble());
        System.out.println("Bimestre 2: " + aluno.getBim2());

        aluno.setBim3(sc.nextDouble());
        System.out.println("Bimestre 3: "+ aluno.getBim3());


        System.out.println(aluno.alunosReprovados());


    }
}
