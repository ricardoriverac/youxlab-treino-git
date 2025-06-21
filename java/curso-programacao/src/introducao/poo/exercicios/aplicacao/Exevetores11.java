package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores11 {
    /// <p style= color:purple> Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
    /// que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
    /// de homens.<p/>
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Quantas pessoas serão digitadas: ");
        int quant = input.nextInt();
        double[] altura = new double[quant];
        char[] sexo = new char[quant];
        double menorA = 0.0, maiorA = 0.0;
        int soma = 0;
        double[] sexoF = new double[quant];
        for (int i = 0; i < quant; i++) {
            input.nextLine();
            System.out.printf("Altura da %d° pessoa: ", i + 1);
            altura[i] = input.nextDouble();
            System.out.printf("Sexo da %d° pessoa: ", i + 1);
            sexo[i] = input.next().charAt(0);
            if (i == 0) {
                maiorA = altura[i];
                menorA = altura[i];
            }
            else{
                if (altura[i] > maiorA){
                    maiorA = altura[i];
                }
                if (altura[i] < menorA){
                    menorA = altura[i];
                }
            }
            if (sexo[i] == 'F' || sexo[i] == 'f'){
                sexoF[i] = altura[i];
                soma += 1;
            }
            if (sexo[i] == 'm' || sexo[i] == 'M'){
                soma += 1;
            }

        }
        System.out.printf("Maior altura: %.2f %n", maiorA);
        System.out.printf("Menor altura: %.2f %n", menorA);

        for (int i = 0; i < sexoF.length; i++) {


        }System.out.println("Total de homens: " + soma);

    }
}
