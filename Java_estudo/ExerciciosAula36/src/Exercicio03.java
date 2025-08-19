import java.util.Scanner;

public class Exercicio03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero1 = sc.nextInt();
        int numero2 = sc.nextInt();

        if (numero1 % numero2 == 0){
            System.out.println("Os números são multiplos");
        }
        else
            System.out.println("Não são");


    }
}

//Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao
//Multiplos", indicando se os valores lidos são múltiplos entre si. Atenção: os números devem poder ser digitados em
//ordem crescente ou decrescente.