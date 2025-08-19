package entidades;

public class PessoaJuridica extends Contribuinte{
    private Integer quantidadeFuncionarios;

    public PessoaJuridica(){
    }
    public PessoaJuridica(String nome, Double anualContribuicao, Integer quantidadeFuncionarios) {
        super(nome, anualContribuicao);
        this.quantidadeFuncionarios = quantidadeFuncionarios;
    }

    public Integer getQuantidadeFuncionarios() {
        return quantidadeFuncionarios;
    }

    public void setQuantidadeFuncionarios(Integer quantidadeFuncionarios) {
        this.quantidadeFuncionarios = quantidadeFuncionarios;
    }
    @Override
    public double taxa() {
        Double taxaBasica;
        if (quantidadeFuncionarios > 10) {
            taxaBasica = getAnualContribuicao() * 0.14;
        } else {
            taxaBasica = getAnualContribuicao() * 0.16;
        }
        return taxaBasica;
    }

}
