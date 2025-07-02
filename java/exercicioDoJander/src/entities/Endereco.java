package entities;

public class Endereco {
    private String rua;
    private String numero;
    private String cidade;
    private String estado;

    public Endereco(){
    }

    public Endereco(String rua, String numero, String cidade, String estado) {
        this.rua = rua;
        this.numero = numero;
        this.cidade = cidade;
        this.estado = estado;
    }

    public String getRua() {
        return rua;
    }

    public void setRua(String rua) {
        this.rua = rua;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    @Override
    public String toString() {
        return "Endereco: " +
                "rua: '" + rua + '\'' +
                ", número: '" + numero + '\'' +
                ", cidade: '" + cidade + '\'' +
                ", estado: '" + estado + '\'';
    }
}
