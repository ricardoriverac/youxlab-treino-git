package introducao.poo.exercicios.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class Exevetores08 {
    /// <p style= color:purple>Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
    /// aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
    /// digitado, mostrar a mensagem "NENHUM NUMERO PAR" </p>
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        System.out.print("Quantos elementos vai ter o vetor: ");
        int quant = input.nextInt();
        int[] array = new int[quant];
        for (int i = 0; i < array.length; i++) {
            System.out.print("Digite o número: ");
            array[i] = input.nextInt();

        }
        int somaPar = 0;
        int quantpar = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 == 0) {
                somaPar += array[i];
                quantpar += 1;
            }
        }
        double mediaPar = 0.0;
        mediaPar = (double) somaPar / quantpar;
        if (quantpar == 0)
            System.out.println("Nenhum par existe");
        else
            System.out.println("Media dos pares: " + mediaPar);
        input.close();
    }
}
