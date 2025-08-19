package model;

import entidades.Contrato;
import entidades.Parcelas;

import java.time.LocalDate;

public class ContratoServico {

    private final OnlinePagamentoServico onlinePagamentoServico;

    public ContratoServico(OnlinePagamentoServico onlinePagamentoServico) {
        this.onlinePagamentoServico = onlinePagamentoServico;
    }

    public void processoContrato(Contrato contrato, Integer quantidadeParcelas) {
        double valorParcela = contrato.getTotalValor() / quantidadeParcelas;

        for (int contador = 1; contador <= quantidadeParcelas; contador++) {
            LocalDate dataParcela = contrato.getData().plusMonths(contador);

            double juro = onlinePagamentoServico.juro(valorParcela, contador);
            double taxaPagamento = onlinePagamentoServico.taxaPagamento(valorParcela + juro);
            double valorTotalParcela = valorParcela + juro + taxaPagamento;

            // Adiciona parcela na lista do contrato
            contrato.getParcelas().add(new Parcelas(dataParcela, valorTotalParcela));
        }

        }
    }

