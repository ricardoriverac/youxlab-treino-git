package entidades;

public class ContaBancaria {
    private Integer numero;
    private String nomeTitular;
    private String senha;
    private Integer saldo;

    public void setNomeTitular(String nome){
        this.nomeTitular = nome;
    }

    public String getNomeTitular(){
        return this.nomeTitular;
    }

    public Integer getNumero() {
        return numero;
    }

    public void setNumero(Integer numero) {
        this.numero = numero;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public Integer getSaldo() {
        return saldo;
    }

    public void setSaldo(Integer saldo) {
        this.saldo = saldo;
    }

    public String toString() {
        return "ContaBancaria{" +
                "numero=" + numero +
                ", nomeTitular='" + nomeTitular + '\'' +
                ", senha='" + senha + '\'' +
                ", saldo=" + saldo +
                '}';
    }
}
