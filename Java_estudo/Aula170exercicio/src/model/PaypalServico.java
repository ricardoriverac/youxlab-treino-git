package model;

public class PaypalServico implements OnlinePagamentoServico {

    public Double taxaPagamento(double valor) {
        return valor * 0.02;
    }

    public Double juro(double valor, int meses) {
        return valor * 0.01 * meses;
    }
}
