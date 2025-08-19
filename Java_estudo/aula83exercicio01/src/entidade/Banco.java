package entidade;

public class Banco {
    private int contaNumero;
    private String nomeUsuario;
    private double saldo;
    private double saldoInicial;

    public Banco(int contaNumero, String nomeUsuario) {
        this.contaNumero = contaNumero;
        this.nomeUsuario = nomeUsuario;

    }

    public int getContaNumero() {
        return this.contaNumero;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }

    public double getSaldo() {
        return saldo;
    }

    public double getSaldoInicial() {
        return saldoInicial;
    }


    public void setNomeUsuario(String nomeUsuario) {
        this.nomeUsuario = nomeUsuario;
    }

    public void setSaldoInicial(double saldoInicialBancoQueVemDePrograma) {
        this.saldo = saldoInicialBancoQueVemDePrograma;
    }
    public double transacaoBancaria(double valor) {
        if (valor < 0) {
            return saldo -= valor * 5/100 + valor;
        } else {
            return saldo += valor * 5/100 + valor;

        }
    }
}
