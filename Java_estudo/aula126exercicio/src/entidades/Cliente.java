package entidades;

import java.util.ArrayList;
import java.util.List;

public class Cliente {
    private String nome;
    private String email;

    private List<Produto> listaProdutos = new ArrayList<>();
    public Cliente(){
    }

    public Cliente(String nome, String email) {
        this.nome = nome;
        this.email = email;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<Produto> getProduto() {
        return listaProdutos;
    }
    public void adicionarProduto(Produto novoProduto) {
        listaProdutos.add(novoProduto);
    }
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente: ").append(nome).append("\n");
        sb.append("Email: ").append(email).append("\n");
        sb.append("Produtos:\n");

        for (Produto p : listaProdutos) {
            sb.append("- ").append(p.getNome())
                    .append(", Preço: R$ ").append(p.getPreco())
                    .append(", Quantidade: ").append(p.getQuantidade())
                    .append("\n");
        }

        double somaTotal = 0;
        for (Produto p : listaProdutos) {
            somaTotal += p.somaTotal();
        }

        sb.append("Soma total dos produtos: R$ ").append(somaTotal);

        return sb.toString();
    }

}
