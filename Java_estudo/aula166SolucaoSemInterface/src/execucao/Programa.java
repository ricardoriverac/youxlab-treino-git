package execucao;

import entidades.AluguelCarro;
import entidades.Veiculo;
import model.service.BrasilTaxaServico;
import model.service.ServicoAluguel;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

        System.out.println("Entre com os dados do aluguel ");

        System.out.print("Modelo do carro: ");
        String carroModelo = sc.nextLine();

        System.out.println("Retirada (dd/MM/yyyy hh:mm): ");
        LocalDateTime inicio = LocalDateTime.parse(sc.nextLine(), fmt);

        System.out.println("Retorno (dd/MM/yyyy hh:mm): ");
        LocalDateTime fim = LocalDateTime.parse(sc.nextLine(), fmt);

        AluguelCarro aluguelCarro = new AluguelCarro(inicio, fim, new Veiculo(carroModelo));

        System.out.println("Entre com o preço por hora: ");
        double precoPorHora = sc.nextDouble();
        System.out.println("Entre com o preço por dia: ");
        double precoPorDia = sc.nextDouble();

        ServicoAluguel servicoAluguel = new ServicoAluguel(precoPorDia, precoPorHora, new BrasilTaxaServico());

        servicoAluguel.processoFatura(aluguelCarro);

        System.out.println("FATURA: ");
        System.out.println("Pagamento básico: " + aluguelCarro.getFatura().getSalarioBasico());
        System.out.println("Imposto: " + aluguelCarro.getFatura().getImposto());
        System.out.println("Pagamento total " + aluguelCarro.getFatura().getTotalPagamento());


        sc.close();

    }
}