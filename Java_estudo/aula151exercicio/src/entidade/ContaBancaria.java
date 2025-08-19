package entidade;

import exececoes.DomainException;

public class ContaBancaria {
    private Integer numeroConta;
    private Double saldo;

    public ContaBancaria() {
    }

    public ContaBancaria(Integer numeroConta, Double saldo) {
        this.numeroConta = numeroConta;
        this.saldo = saldo;
    }

    public Integer getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(Integer numeroConta) {
        this.numeroConta = numeroConta;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public boolean saque(double saque) {
        if (saque <= 0) {
            throw new DomainException("Valor para saque insuficiente ");
        }
        else if (saldo < saque) {
            throw new DomainException("O saque não pode vir a ser efetuado ");
        } else {
            saldo -= saque;
        }
        return false;
    }
}
