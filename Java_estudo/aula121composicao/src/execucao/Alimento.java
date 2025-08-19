package execucao;

public class Alimento {
    private String nome;
    private Double calorias;
    private TipoAlimento tipoAlimento;
    private Receita receita;

    public Receita getReceita () {
        return receita;
    }

    public void setReceita(Receita receitaQueUsuarioDigitou) {
        this.receita = receitaQueUsuarioDigitou;
    }
}
