import java.util.Locale;
import java.util.Scanner;

public class exercicio01 {

public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);

    int largura = sc.nextInt();
    int comprimento = sc.nextInt();
    int soma = largura + comprimento;



    System.out.printf("A soma é = "+ soma);
    }
}

//Faça um programa para ler dois valores inteiros, e depois mostrar na tela a soma desses números com uma
//mensagem explicativa, conforme exemplos

