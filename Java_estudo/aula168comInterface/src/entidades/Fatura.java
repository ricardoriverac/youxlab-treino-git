package entidades;

public class Fatura {
    private Double precoBasico;
    private Double imposto;

    public Fatura(){
    }

    public Fatura(Double precoBasico, Double imposto) {
        this.precoBasico = precoBasico;
        this.imposto = imposto;
    }

    public Double getSalarioBasico() {
        return precoBasico;
    }

    public void setSalarioBasico(Double precoBasico) {
        this.precoBasico = precoBasico;
    }

    public Double getImposto() {
        return imposto;
    }

    public void setImposto(Double imposto) {
        this.imposto = imposto;
    }
    public Double getTotalPagamento(){
        return getSalarioBasico() + getImposto();
    }
}
