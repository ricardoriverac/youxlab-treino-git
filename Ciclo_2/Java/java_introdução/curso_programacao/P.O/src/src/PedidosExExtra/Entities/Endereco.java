package PedidosExExtra.Entities;

public class Endereco {
    private String rua;
    private String numero;
    private String cidade;
    private String estado;

    public Endereco(String rua, String estado, String cidade, String numero) {
        this.rua = rua;
        this.estado = estado;
        this.cidade = cidade;
        this.numero = numero;
    }

    public String getRua() {
        return rua;
    }

    public void setRua(String rua) {
        this.rua = rua;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    @Override
    public String toString() {
        return "Endereco = " +
                "| rua = " + rua +
                "| numero = " + numero +
                "| cidade = " + cidade +
                "| estado = " + estado;
    }
}
