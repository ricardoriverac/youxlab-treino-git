package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores09 {
    /// <p style= color:purple> Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
    /// devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
    /// da pessoa mais velha. </p>
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Quantas pessoas você vai digitar: ");
        int quant = input.nextInt();
        String[] nome = new String[quant];
        int[] idade = new int[quant];
        int maiorIdade = 0;
        for (int i = 0; i < quant; i++) {
            input.nextLine();
            System.out.printf("Dados da %d pessoa%n" , i+1);
            System.out.print("Nome: ");
            nome[i] = input.nextLine();
            System.out.print("Idade: ");
            idade[i] = input.nextInt();
            if (idade[i] > maiorIdade){
                maiorIdade = idade[i];
            }
        }
        System.out.print("Pessoa mais velha: ");
        for (int i = 0; i < nome.length; i++) {
            if (idade[i] == maiorIdade){
                System.out.println(nome[i]);
            }
        }






        input.close();
    }
}
