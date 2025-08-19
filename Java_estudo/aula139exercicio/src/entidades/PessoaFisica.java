package entidades;

public class PessoaFisica extends Contribuinte {

    private Double gastoSaude;

    public PessoaFisica(){
    }

    public PessoaFisica(String nome, Double anualContribuicao, Double gastoSaude) {
        super(nome, anualContribuicao);
        this.gastoSaude = gastoSaude;
    }

    public Double getGastoSaude() {
        return gastoSaude;
    }

    public void setGastoSaude(Double gastoSaude) {
        this.gastoSaude = gastoSaude;
    }

    @Override
    public double taxa() {
        Double taxaBasica;

        if (getAnualContribuicao() < 20000) {
            taxaBasica = getAnualContribuicao() * 0.15;
        } else {
            taxaBasica = getAnualContribuicao() * 0.25;
        }
        if (gastoSaude != null && gastoSaude > 0) {
            taxaBasica = gastoSaude / 50 + getAnualContribuicao();
        }
        return taxaBasica;

    }
}
