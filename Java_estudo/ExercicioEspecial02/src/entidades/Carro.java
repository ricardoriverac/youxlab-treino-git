package entidades;

public class Carro extends Veiculo{
    public Carro(String nomeVeiculo, String modelo, Integer placa, Double precoPorDia) {
        super(nomeVeiculo, modelo, placa, precoPorDia);
    }
    @Override
    public String mover(String x, String y) {
        return "O carro se moveu de X: " + x + " até " + " a posição Y: " + y;
    }

    @Override
    public Double calcularPreco(Integer dias, Double precoPorDia) {
        double valor = dias * precoPorDia;
        return (valor * 10)/100 + valor;
    }
}
