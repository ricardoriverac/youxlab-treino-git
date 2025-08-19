package model;

public interface OnlinePagamentoServico {
    Double taxaPagamento(double valor);
    Double juro(double valor,int meses);
}
