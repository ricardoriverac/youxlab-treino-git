package execucao;

import entidades.Produto;
import entidades.ProdutoNovo;
import entidades.ProdutoUsado;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        List<Produto> listaProdutos = new ArrayList<>();

        System.out.print("Quantos Produtos deseja?: ");
        int quantidade = sc.nextInt();
        sc.nextLine();

        for (int contador = 0; contador < quantidade; contador++) {
            System.out.println("Produto #" + (contador + 1) + " dados:");
            System.out.print("O produto é comum, usado ou importado (c/u/i)? ");
            char tipoProduto = sc.next().charAt(0);
            sc.nextLine();

            System.out.print("Nome: ");
            String nome = sc.nextLine();

            System.out.print("Preço: ");
            Double preco = sc.nextDouble();
            sc.nextLine();

            Produto produto;
            if (tipoProduto == 'u') {
                System.out.print("Data de fabricação (dd/MM/yyyy): ");
                String dataString = sc.nextLine();
                LocalDate dataFabricacao = LocalDate.parse(dataString, formato);

                produto = new ProdutoUsado(nome, preco, dataFabricacao);

            } else if (tipoProduto == 'i') {
                System.out.print("Taxa de importação: ");
                double taxa = sc.nextDouble();
                sc.nextLine();

                produto = new ProdutoNovo(nome, preco, taxa);

            } else {
                produto = new Produto(nome, preco);
            }

            listaProdutos.add(produto);
        }

        System.out.println("Etiquetas de preço:");
        for (Produto p : listaProdutos) {
            p.entiqueta();
        }

        sc.close();
    }
}
