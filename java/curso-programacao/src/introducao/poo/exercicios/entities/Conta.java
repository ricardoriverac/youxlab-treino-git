package introducao.poo.exercicios.entities;

public class Conta {
    private String nomeUsuario;
    private int numeroConta;
    private double saldo = 0;

    public Conta(int numeroConta , String nomeUsuario){
        this.numeroConta = numeroConta;
        this.nomeUsuario = nomeUsuario;
    }

    public void depositar(double deposito){
        this.saldo += deposito;
    }
    public void saque(double saque){
        this.saldo -= saque + 5;
    }
    public String toString(){
        return numeroConta
                + ", Holder "
                + nomeUsuario
                + ", Balance "
                + saldo;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }

    public void setNomeUsuario(String nomeUsuario) {
        this.nomeUsuario = nomeUsuario;
    }

    public int getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(int numeroConta) {
        this.numeroConta = numeroConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
}
