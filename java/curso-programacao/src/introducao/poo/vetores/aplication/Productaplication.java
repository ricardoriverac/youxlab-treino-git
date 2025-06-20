package introducao.poo.vetores.aplication;

import introducao.poo.vetores.entities.Product;

import java.util.Locale;
import java.util.Scanner;

public class Productaplication {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        int quantidade = input.nextInt();
        Product[] array = new Product[quantidade];
        for (int i = 0; i < array.length; i++) {
            input.nextLine();
            System.out.print("Nome: ");
            String nome = input.nextLine();
            System.out.print("Preço: ");
            double preco = input.nextDouble();
            array[i] = new Product(nome , preco);

        }
        double sum = 0.0;
        for (int i = 0; i < array.length; i++) {
            sum += array[i].getPreco();
        }
        double avg = sum / array.length;
        System.out.println(avg);
    }
}
