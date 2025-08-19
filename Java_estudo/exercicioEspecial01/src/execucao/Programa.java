package execucao;

import entidade.*;
import entidade.Status;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Cliente c1 = new Cliente(1, "Gabriel", "joao@email.com");
        Cliente c2 = new Cliente(2, "Nicolas", "maria@email.com");
        Cliente c3 = new Cliente(3, "Ana", "carlos@email.com");
        Cliente c4 = new Cliente(4, "Eduardo", "ana@email.com");
        Cliente c5 = new Cliente(5, "Rafaela", "pedro@email.com");

        Produto p1 = new Produto(1, "Tv", 1000);
        Produto p2 = new Produto(2, "Celular", 2000);
        Produto p3 = new Produto(3, "Computador", 3000);
        Produto p4 = new Produto(4, "Tablet", 4000);
        Produto p5 = new Produto(5, "Óculos", 5000);
        Produto p6 = new Produto(6, "Monitor", 6000);

        Endereco ed1 = new Endereco("Vila Nova", 100, "Lavras", "MG");
        Endereco ed2 = new Endereco("Vila Rica", 100, "Belo Horizonte", "RS");
        Endereco ed3 = new Endereco("Vila Velha", 100, "Carvalho", "ES");
        Endereco ed4 = new Endereco("São Vicente", 100, "Campo Belo", "SC");
        Endereco ed5 = new Endereco("Água Limpa", 100, "São Paulo", "SP");

        List<Pedido> listaPedidos = new ArrayList<>();

        Pedido pedido1 = new Pedido(1, c1, ed1, Status.EM_ANDAMENTO);
        pedido1.adicionarProduto(p1);
        pedido1.adicionarProduto(p2);
        listaPedidos.add(pedido1);

        Pedido pedido2 = new Pedido(2, c3, ed2,Status.ENTREGUE);
        pedido2.adicionarProduto(p3);
        listaPedidos.add(pedido2);

        Pedido pedido3 = new Pedido(3, c5, ed3,Status.ATRASADO);
        pedido3.adicionarProduto(p1);
        pedido3.adicionarProduto(p4);
        listaPedidos.add(pedido3);

        Pedido pedido4 = new Pedido(4, c2, ed4,Status.AGUARDANDO_ENVIO);
        pedido4.adicionarProduto(p5);
        listaPedidos.add(pedido4);

        Pedido pedido5 = new Pedido(5, c1, ed5,Status.EM_ANDAMENTO);
        pedido5.adicionarProduto(p2);
        pedido5.adicionarProduto(p6);
        listaPedidos.add(pedido5);

        int opcao = 0;
        while (opcao != 4) {
            System.out.println("Escolha uma das opções abaixo:");
            System.out.println("1 - Buscar pedido por ID");
            System.out.println("2 - Ver valor total do pedido por ID");
            System.out.println("3 - Buscar pedidos por Status");
            System.out.println("4 - Sair");

            opcao = sc.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Digite o ID do pedido: ");

                    int idBusca = sc.nextInt();

                    int i;
                    for (i = 0; i < listaPedidos.size(); i++) {
                        if (listaPedidos.get(i).getId() == idBusca) {
                            System.out.println(listaPedidos.get(i));
                        }
                    }
                    if (i == listaPedidos.size()) {
                        System.out.println("Pedido não encontrado.");
                    }
                    break;

                case 2:
                    System.out.print("Digite o ID do pedido: ");

                    int idValor = sc.nextInt();

                    boolean achou = false;
                    for (Pedido p : listaPedidos) {
                        if (p.getId() == idValor) {
                            System.out.println("Valor total do pedido: R$ " + p.valorTotal());
                            achou = true;
                            break;
                        }
                    }
                    if (!achou) {
                        System.out.println("Pedido não encontrado.");
                    }
                    break;

                case 3:
                    System.out.println("Escolha o status:");
                    System.out.println("1 - AGUARDANDO_ENVIO");
                    System.out.println("2 - EM_ANDAMENTO");
                    System.out.println("3 - ATRASADO");
                    System.out.println("4 - ENTREGUE");
                    int statusEscolhido = sc.nextInt();
                   Status statusBuscado = null;
                    switch (statusEscolhido) {
                        case 1:
                            statusBuscado =Status.AGUARDANDO_ENVIO;
                            break;
                        case 2:
                            statusBuscado =Status.EM_ANDAMENTO;
                            break;
                        case 3:
                            statusBuscado =Status.ATRASADO;
                            break;
                        case 4:
                            statusBuscado =Status.ENTREGUE;
                            break;
                        default:
                            System.out.println("Status inválido.");
                    }
                    if (statusBuscado != null) {
                        for (Pedido p : listaPedidos) {
                            if (p.getStatus() == statusBuscado) {
                                System.out.println(p);
                            }
                        }
                    }
                    break;

                case 4:
                    System.out.println("Saindo...");
                    break;

                default:
                    System.out.println("Opção inválida.");
            }
        }

        sc.close();
    }
}
