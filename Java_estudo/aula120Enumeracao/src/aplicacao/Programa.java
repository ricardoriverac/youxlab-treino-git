package aplicacao;

import entidade.OrderStatus;
import entidades.Pedido;

import java.util.Date;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Pedido pedido = new Pedido(1080, new Date(), OrderStatus.AguardandoPagamento);
        System.out.println(pedido);

        int opcao = 0;
        while (opcao != 4) {
            System.out.println("Seu status atual e: " + pedido.getStatus());
            System.out.println("Escolha uma das opções abaixo:");
            System.out.println("1 - Alterar id ");
            System.out.println("2 - Mudar Status atual ");
            System.out.println("3 - Finalizar ");

            opcao = sc.nextInt();
            if (opcao == 1) {
                System.out.println("Digite para qual id deseja alterar: ");
                int novoId = sc.nextInt();
                pedido.setId(novoId);

            } else if (opcao == 2) {
                System.out.println("Escolha o novo status:");
                String status = sc.next();
                OrderStatus os = OrderStatus.valueOf(status);
                pedido.setStatus(os);
            }
            else if (opcao == 3)
                break;
            }

        }

    }


