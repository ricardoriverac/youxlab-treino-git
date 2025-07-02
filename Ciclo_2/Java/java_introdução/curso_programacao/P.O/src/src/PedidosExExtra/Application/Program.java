package PedidosExExtra.Application;

import PedidosExExtra.Entities.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        List<Pedido> ListaPedidos = new ArrayList<>();
        Scanner input = new Scanner(System.in);

        CLiente cLiente0 = new CLiente(0, "Ana Bezerra", "ana.bezerra@gmail.com");
        Endereco endereco0 = new Endereco("Rua das Palmeiras", "São Paulo", "São Paulo", "210");
        Produto produto0 = new Produto(0, "Fone Bluetooth Max", 99.90);
        Pedido pedido0 = new Pedido(0, StatusPedido.ENTREGUE, endereco0, cLiente0);

        CLiente cLiente1 = new CLiente(1, "Bruno Carvalho", "bruno.carvalho@yahoo.com");
        Endereco endereco1 = new Endereco("Rua dos Jasmins", "Rio de Janeiro", "Rio de Janeiro", "315");
        Produto produto1 = new Produto(1, "Teclado Mecânico RGB", 159.00);
        Pedido pedido1 = new Pedido(1, StatusPedido.EM_ANDAMENTO, endereco1, cLiente1);

        CLiente cLiente2 = new CLiente(2, "Carla Dias", "carla.dias@outlook.com");
        Endereco endereco2 = new Endereco("Rua Sete de Setembro", "Bahia", "Salvador", "480");
        Produto produto2 = new Produto(2, "Garrafa Térmica 1 L", 39.50);
        Pedido pedido2 = new Pedido(2, StatusPedido.AGUARDANDO_ENVIO, endereco2, cLiente2);

        CLiente cLiente3 = new CLiente(3, "Diego Esteves", "diego.esteves@gmail.com");
        Endereco endereco3 = new Endereco("Rua das Andorinhas", "Minas Gerais", "Belo Horizonte", "55");
        Produto produto3 = new Produto(3, "Mochila Anti-Furto", 129.99);
        Pedido pedido3 = new Pedido(3, StatusPedido.ATRASADO, endereco3, cLiente3);

        CLiente cLiente4 = new CLiente(4, "Elisa Ferreira", "elisa.ferreira@bol.com.br");
        Endereco endereco4 = new Endereco("Avenida Atlântica", "Paraná", "Curitiba", "1020");
        Produto produto4 = new Produto(4, "Smartwatch FitPro", 349.90);
        Pedido pedido4 = new Pedido(4, StatusPedido.AGUARDANDO_ENVIO, endereco4, cLiente4);

        CLiente cLiente5 = new CLiente(5, "Felipe Gomes", "felipe.gomes@uol.com.br");
        Endereco endereco5 = new Endereco("Rua do Imperador", "Pernambuco", "Recife", "230");
        Produto produto5 = new Produto(5, "Livro “Java para Iniciantes”", 29.90);
        Pedido pedido5 = new Pedido(5, StatusPedido.ENTREGUE, endereco5, cLiente5);

        CLiente cLiente6 = new CLiente(6, "Gabriela Henrique", "gabriela.henrique@hotmail.com");
        Endereco endereco6 = new Endereco("Rua das Laranjeiras", "Ceará", "Fortaleza", "890");
        Produto produto6 = new Produto(6, "Monitor 24″ IPS", 499.00);
        Pedido pedido6 = new Pedido(6, StatusPedido.EM_ANDAMENTO, endereco6, cLiente6);

        CLiente cLiente7 = new CLiente(7, "Heitor Iglesias", "heitor.iglesias@protonmail.com");
        Endereco endereco7 = new Endereco("Rua Benedito Calixto", "Santa Catarina", "Florianópolis", "310");
        Produto produto7 = new Produto(7, "Cafeteira Elétrica Compact", 79.00);
        Pedido pedido7 = new Pedido(7, StatusPedido.ATRASADO, endereco7, cLiente7);

        CLiente cLiente8 = new CLiente(8, "Isabela Jara", "isabela.jara@icloud.com");
        Endereco endereco8 = new Endereco("Rua Dom Pedro II", "Rio Grande do Sul", "Porto Alegre", "444");
        Produto produto8 = new Produto(8, "Furadeira de Impacto 650 W", 219.90);
        Pedido pedido8 = new Pedido(8, StatusPedido.ENTREGUE, endereco8, cLiente8);

        CLiente cLiente9 = new CLiente(9, "João Kauer", "joao.kauer@gmail.com");
        Endereco endereco9 = new Endereco("Rua das Acácias", "Goiás", "Goiânia", "678");
        Produto produto9 = new Produto(9, "Luminária LED USB", 19.90);
        Pedido pedido9 = new Pedido(9, StatusPedido.AGUARDANDO_ENVIO, endereco8, cLiente8);

        CLiente cLiente10 = new CLiente(10, "Larissa Lima", "larissa.lima@live.com");
        Endereco endereco10 = new Endereco("Avenida Getúlio Vargas", "Distrito Federal", "Brasília", "900");
        Produto produto10 = new Produto(10, "Notebook UltraSlim 14″", 2599.00);
        Pedido pedido10 = new Pedido(10, StatusPedido.ATRASADO, endereco10, cLiente10);


        pedido0.addProduto(produto0);
        pedido1.addProduto(produto1);
        pedido2.addProduto(produto2);
        pedido3.addProduto(produto3);
        pedido4.addProduto(produto4);
        pedido5.addProduto(produto5);
        pedido6.addProduto(produto6);
        pedido7.addProduto(produto7);
        pedido8.addProduto(produto8);
        pedido9.addProduto(produto9);
        pedido10.addProduto(produto10);

        ListaPedidos.add(pedido0);
        ListaPedidos.add(pedido1);
        ListaPedidos.add(pedido2);
        ListaPedidos.add(pedido3);
        ListaPedidos.add(pedido4);
        ListaPedidos.add(pedido5);
        ListaPedidos.add(pedido6);
        ListaPedidos.add(pedido7);
        ListaPedidos.add(pedido8);
        ListaPedidos.add(pedido9);
        ListaPedidos.add(pedido10);


        while (true) {

            System.out.println("Qual o id do pedido?");
            int id = input.nextInt();
            for (Pedido pedido : ListaPedidos) {
                if (id == pedido.getId(id)) {
                    System.out.println(pedido.toString());
                    System.out.println("Valor total dos produtos vendidos: " + pedido.valorTotal());
                }
            }

            System.out.println();
            System.out.println("""
                    Quais tipos de status dos pedidos que você quer ver?\
                    
                    [AGUARDANDO_ENVIO]
                    [EM_ANDAMENTO]
                    [ATRASADO]
                    [ENTREGUE]""");
            System.out.print("Digite o status: ");
            String status = input.next();
            StatusPedido staatusPedido = StatusPedido.valueOf(status.toUpperCase());
            for (Pedido pedido : ListaPedidos) {
                if (staatusPedido == pedido.getStatus()) {
                    System.out.println("Cliente: " + pedido.getNome().getNome());
                    System.out.println("Status do pedido: " + pedido.getStatus());
                    System.out.println();
                }
            }

            input.nextLine();
            System.out.println("Gostaria de continuar? S/N");
            String continuarNS = input.nextLine().toUpperCase();

            if (continuarNS.equals("N")){
                break;
            }

        }
        System.out.println("Até mais!");
    }
}

