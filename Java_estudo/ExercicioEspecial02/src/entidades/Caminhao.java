package entidades;

public class Caminhao extends Veiculo{
    public Caminhao(String nomeVeiculo, String modelo, Integer placa, Double precoPorDia) {
        super(nomeVeiculo, modelo, placa, precoPorDia);

    }
    @Override
    public String mover(String x,String y){
        return "O caminhão se moveu de X: " + x + " até " + " a posição Y: " + y;
    }
    @Override
    public Double calcularPreco(Integer dias, Double precoPorDia){
        double valor = dias * precoPorDia;
        return (valor * 0.20)/100;
    }

}
