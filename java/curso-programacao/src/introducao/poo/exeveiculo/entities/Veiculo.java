package introducao.poo.exeveiculo.entities;

public abstract class Veiculo {

    private String modelo;
    private String placa;
    private Double precoPorDia;

    public Veiculo(){
    }

    public Veiculo(String modelo, String placa, Double precoPorDia) {
        this.modelo = modelo;
        this.placa = placa;
        this.precoPorDia = precoPorDia;
    }


    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public Double getPrecoPorDia() {
        return precoPorDia;
    }

    public void setPrecoPorDia(Double precoPorDia) {
        this.precoPorDia = precoPorDia;
    }

    public void mover(int x , int y){
    }

    public abstract double calcularPreco(int dias);
}
