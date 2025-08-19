package execucao;

import entidades.Contrato;
import entidades.Parcelas;
import entidades.Parcelas;
import model.ContratoServico;
import model.PaypalServico;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

        System.out.println("Entre com os dados do contrato: ");

        System.out.print("Número: ");
        Integer numero = sc.nextInt();
        sc.nextLine(); // limpa o \n pendente

        System.out.print("Data (dd/MM/yyyy HH:mm): ");
        String dataStr = sc.nextLine();
        LocalDateTime data = LocalDateTime.parse(dataStr, fmt);

        System.out.print("Valor do contrato: ");
        Double totalValor = sc.nextDouble();

        Contrato contrato = new Contrato(numero, data, totalValor);

        System.out.print("Entre com o número de parcelas: ");
        Integer numeroParcelas = sc.nextInt();

        // Cria o serviço de pagamento PayPal e o serviço do contrato
        ContratoServico contratoServico = new ContratoServico(new PaypalServico());

        // Processa o contrato com o número de parcelas informado
        contratoServico.processoContrato(contrato, numeroParcelas);

        // Imprime as parcelas geradas
        System.out.println("Parcelas:");
        for (Parcelas parcela : contrato.getParcelas()) {
            System.out.println(parcela);
        }

        sc.close();
    }
}
