import entities.Aluno;

import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Set<Aluno> alunos = new TreeSet<>();
        System.out.print("How many students for course A: ");
        int cA = input.nextInt();
        for (int i = 0; i < cA; i++) {
            Aluno aluno = new Aluno(input.nextInt());
            alunos.add(aluno);
        }
        System.out.print("How many students for course B: ");
        int cB = input.nextInt();
        for (int i = 0; i < cB; i++) {
            Aluno aluno = new Aluno(input.nextInt());
            alunos.add(aluno);
        }
        System.out.print("How many students for course C: ");
        int cC = input.nextInt();
        for (int i = 0; i < cC; i++) {
            Aluno aluno = new Aluno(input.nextInt());
            alunos.add(aluno);
        }
        System.out.println("Total students: "+alunos.size());
    }
}