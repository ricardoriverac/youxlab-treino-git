package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores10 {
    ///  <p style= color:purple> Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
    /// no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
    /// os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
    /// igual a 6.0 (seis). </p>
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Quantos alunos serão digitados: ");
        int quant = input.nextInt();
        String[] nome = new String[quant];
        double[] nota1 = new double[quant];
        double[] nota2 = new double[quant];
        double[] somanota = new double[quant];
        double[] media = new double[quant];

        for (int i = 0; i < quant; i++) {
            input.nextLine();
            System.out.printf("Digite o nome, primeira e segunda nota do %d° aluno %n" , i+1);
            System.out.print("Nome: ");
            nome[i] = input.nextLine();
            System.out.print("Nota 1: ");
            nota1[i] = input.nextDouble();
            System.out.print("Nota 2: ");
            nota2[i] = input.nextDouble();
        }
        for (int i = 0; i < quant; i++) {
            somanota[i] = nota1[i] += nota2[i];
            media[i] = somanota[i] /= 2;
        }
        System.out.println("Aluno aprovados: ");
        for (int i = 0; i < quant; i++) {
            if (media[i] >= 6.0){
                System.out.println(nome[i]);
            }
        }
        input.close();
    }
}
