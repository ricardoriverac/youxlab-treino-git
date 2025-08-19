package entidades;

public class Moto extends Veiculo {
    public Moto(String nomeVeiculo, String modelo, Integer placa, Double precoPorDia) {
        super(nomeVeiculo, modelo, placa, precoPorDia);
    }

    @Override
    public String mover(String x, String y) {
        return "A moto se moveu de X: " + x + " até " + " a posição Y: " + y;
    }

    @Override
    public Double calcularPreco(Integer dias, Double precoPorDia) {
        double valor = dias * precoPorDia;
        return valor - (valor * 5/100);
    }

}
