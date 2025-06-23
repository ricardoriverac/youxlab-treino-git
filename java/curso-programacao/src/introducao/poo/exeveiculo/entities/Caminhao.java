package introducao.poo.exeveiculo.entities;

public class Caminhao extends Veiculo {

    public Caminhao() {
    }

    public Caminhao(String modelo, String placa, Double precoPorDia) {
        super(modelo, placa, precoPorDia);
    }

    @Override
    public void mover(int x, int y) {
        System.out.println("THUCUTHUCUU");
        System.out.printf("Seu caminhão está na coordenada %d  %d%n", x , y);
    }

    @Override
    public double calcularPreco(int dias) {
        return getPrecoPorDia() * dias * 1.20;
    }
}
