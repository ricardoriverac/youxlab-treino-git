package model.service;

import entidades.AluguelCarro;
import entidades.Fatura;

import java.time.Duration;

public class ServicoAluguel {
    private Double precoHora;
    private Double precoDIa;

    private BrasilTaxaServico taxaServico;

    public ServicoAluguel(Double precoHora, Double precoDIa, BrasilTaxaServico taxaServico) {
        this.precoHora = precoHora;
        this.precoDIa = precoDIa;
        this.taxaServico = taxaServico;
    }
    public void processoFatura(AluguelCarro aluguelCarro){
        double minutos = Duration.between(aluguelCarro.getInicio(),aluguelCarro.getFim()).toMinutes();
        double horas = minutos / 60.0;

        double pagamentoBasico;
        if (horas <= 12.0){
            pagamentoBasico = precoHora * Math.ceil(horas);
        }
        else{
            pagamentoBasico = precoDIa * Math.ceil(horas/24.0);

        }
        double imposto = taxaServico.imposto(pagamentoBasico);

        aluguelCarro.setFatura(new Fatura(pagamentoBasico,imposto));
    }
}
