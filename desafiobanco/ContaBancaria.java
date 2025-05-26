package desafiobanco;
public class ContaBancaria{
    int numero;
    String titular;
    double saldo;

    public ContaBancaria(int numeroConta, String titular, double saldo){
        this.numero = numeroConta;
        this.titular = titular;
        this.saldo = saldo;
    }

    void depositar(double valor){
        saldo += valor;
    }

    void sacar(double valor){
        if(valor <= saldo){
            saldo -= valor;
            System.out.println("Saque realizado com sucesso " + "No valor de: " + valor);
            System.out.println(saldo);
        }
    }

    void mostrarConta(){
        System.out.println("Número da conta: " + numero);
        System.out.println("Titular: " + titular);
        System.out.println("Saldo Atual: " + (int) saldo);
    }

    @Override
    public String toString(){
        return "{ " + titular + ", " + numero + ", " + saldo + " }";
    }
}