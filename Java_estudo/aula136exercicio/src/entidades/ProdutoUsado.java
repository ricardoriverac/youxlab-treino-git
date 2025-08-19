package entidades;

import java.time.LocalDate;
import java.util.Date;

public final class  ProdutoUsado extends Produto{
    private LocalDate fabricacaoData;

    public ProdutoUsado(){
    }

    public ProdutoUsado(String nome, Double preco, LocalDate fabricacaoData) {
        super(nome, preco);
        this.fabricacaoData = fabricacaoData;
    }
    @Override
    public String entiqueta() {
        String texto = fabricacaoData + " " + preco;
        return texto;
    }
}
