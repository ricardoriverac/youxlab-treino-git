package introducao.poo.exeveiculo.entities;

public class Moto extends Veiculo {

    public Moto() {
    }

    public Moto(String modelo, String placa, Double precoPorDia) {
        super(modelo, placa, precoPorDia);
    }

    @Override
    public void mover(int x, int y) {
        System.out.println("RAMMDADAAADADAMM");
        System.out.printf("Sua moto está na coordenada %d  %d%n", x , y);
    }

    @Override
    public double calcularPreco(int dias) {
        return getPrecoPorDia() * dias * 00.5;
    }
}
