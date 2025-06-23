package introducao.poo.aplicacao;

import introducao.poo.entities.Product;

import java.util.Locale;
import java.util.Scanner;

public class aplicandoProduct {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Product produto = new Product();

        System.out.println("-Entrada de produto-");
        System.out.print("Nome do produto: " );
        produto.nome = sc.nextLine();
        System.out.print("Preço do produto: ");
        produto.preco = sc.nextDouble();
        System.out.print("Quantidade em estoque: ");
        produto.quantidade = sc.nextInt();

        System.out.println("Produto: " + produto);
        System.out.print("Adicione mais unidade ao produto: ");
        int quantidade = sc.nextInt();
        produto.addprodutos(quantidade);
        System.out.println("Produto: " + produto);
        System.out.print("Remover unidade: ");
        quantidade = sc.nextInt();
        produto.removeprodutos(quantidade);
        System.out.println("Produto: " + produto);
        sc.close();
    }
}
