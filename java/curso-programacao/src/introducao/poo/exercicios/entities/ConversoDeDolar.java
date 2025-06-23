package introducao.poo.exercicios.entities;

public class ConversoDeDolar {
    public static final double IOF = 6;

    public static double conversorfordolar(double valor , double valor2) {
        double multiplica = valor * valor2;
        double porcetagemdoDolar = multiplica + (multiplica * IOF / 100);
        return porcetagemdoDolar;
    }
}

