package entidades;

public abstract class Contribuinte {
    private String nome;
    private Double anualContribuicao;

    public Contribuinte() {
    }

    public Contribuinte(String nome, Double anualContribuicao) {
        this.nome = nome;
        this.anualContribuicao = anualContribuicao;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Double getAnualContribuicao() {
        return anualContribuicao;
    }

    public void setAnualContribuicao(Double anualContribuicao) {
        this.anualContribuicao = anualContribuicao;
    }

    public abstract double taxa();
}
