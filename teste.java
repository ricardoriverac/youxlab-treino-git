import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class teste{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        List <Number> numeros = new ArrayList<>();

        System.out.print("Digite o primeiro número: ");

        int num1 = input.nextInt();
        numeros.add(num1);

        System.out.print("Digite o segundo número: ");

        int num2 = input.nextInt();
        numeros.add(num2);
        
        int soma = num1 + num2;

        int media = (num1 + num2) / numeros.size();

        System.out.println("A soma é: " + soma);
        System.out.println("A média é: " + media);
        // System.out.println("O primeiro numero da lista é: " numeros.get(0));
        System.out.println("O tamanho da lista é: " + numeros.size());
    }
}
// public class Main {
//     public static void main(String [] args){
//         System.out.println("Olá mundo!");
//     }
// }


// public class somar{
//     public static void main(String[] args){
//         System.out.println("Olá mundo!");

//         int num1 = 5;
//         int num2 = 6;
//         int soma = num1 + num2;

//         System.out.println("A soma é: " + soma);
//     }
    

// }





