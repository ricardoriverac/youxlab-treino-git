package entidades;

public final class ProdutoNovo extends Produto{

    private double valorImportacao;

    public ProdutoNovo(){
    }

    public ProdutoNovo(String nome, Double preco) {
        super(nome, preco);
    }

    public ProdutoNovo(String nome, Double preco, double taxa) {

    }

    public double getValor() {
        return valorImportacao;
    }

    public void setValor(double valor) {
        this.valorImportacao = valor;
    }
    @Override
    public String entiqueta() {

        String texto = valorImportacao + " " + getNome();
        return texto;

    }
}
