package introducao.poo.exeveiculo.entities;

public class Carro extends Veiculo {

    public Carro() {
    }

    public Carro(String modelo, String placa, Double precoPorDia) {
        super(modelo, placa, precoPorDia);
    }

    @Override
    public void mover(int x, int y) {
        System.out.println("VRUMMMMMM");
        System.out.printf("Seu carro está na coordenada %d  %d%n", x , y);

    }

    @Override
    public double calcularPreco(int dias) {
        return getPrecoPorDia() * dias * 1.10;
    }
}
