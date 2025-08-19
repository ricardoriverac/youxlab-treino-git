package entidades;

public abstract class Veiculo {
    private String nomeVeiculo;
    private String modelo;
    private Integer placa;
    private Double precoPorDia;

    public Veiculo() {
    }

    public Veiculo(String nomeVeiculo, String modelo, Integer placa, Double precoPorDia) {
        this.nomeVeiculo = nomeVeiculo;
        this.modelo = modelo;
        this.placa = placa;
        this.precoPorDia = precoPorDia;
    }

    public String getNomeVeiculo() {
        return nomeVeiculo;
    }

    public void setNomeVeiculo(String nomeVeiculo) {
        this.nomeVeiculo = nomeVeiculo;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public Integer getPlaca() {
        return placa;
    }

    public void setPlaca(Integer placa) {
        this.placa = placa;
    }

    public Double getPrecoPorDia() {
        return precoPorDia;
    }

    public void setPrecoPorDia(Double precoPorDia) {
        this.precoPorDia = precoPorDia;
    }

    public abstract String mover(String x, String y);

    public abstract Double calcularPreco(Integer dias, Double precoPorDia);
}

