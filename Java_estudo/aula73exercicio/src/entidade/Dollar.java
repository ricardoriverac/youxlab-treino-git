package entidade;

public class Dollar {
    public static double valorDollar;
    public static double quantidade;

    public static double CotacaoTotal() {
        return quantidade * valorDollar;
    }

}
