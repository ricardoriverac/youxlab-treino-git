package execucao;

import entidades.Cliente;
import entidades.Produto;

import java.util.Date;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Date data = new Date();

        System.out.println("A data na hora do pedido: " + data);

        System.out.println("Nome do cliente: ");
        String nome = sc.nextLine();

        System.out.println("Email: ");
        String email = sc.nextLine();

        Cliente cliente = new Cliente(nome, email);

        System.out.println("Quantidade de produtos que deseja adicionar: ");
        int quantidade = sc.nextInt();

        for(int contador = 0; contador < quantidade; contador++) {
            sc.nextLine();

            System.out.println("Nome do produto " + (contador + 1) + ": ");
            String nomeProduto = sc.nextLine();

            System.out.println("Preço do produto: ");
            double preco = sc.nextDouble();

            System.out.println("Quantidade do produto: ");
            int qtd = sc.nextInt();

            Produto produto = new Produto(nomeProduto, preco, qtd);
            cliente.adicionarProduto(produto);
        }

        System.out.println("\nResumo do pedido:");
        System.out.println(cliente);

        sc.close();
    }
}

