package PedidosExExtra.Entities;

import java.util.ArrayList;
import java.util.List;

public class Pedido {
    private int id;
    private CLiente nome;
    private List<Produto> produtos = new ArrayList<>();
    private Endereco enderecoEntrega;
    private StatusPedido status;

    public Pedido(int id, StatusPedido status, Endereco enderecoEntrega, CLiente nome) {
        this.id = id;
        this.status = status;
        this.enderecoEntrega = enderecoEntrega;
        this.nome = nome;
    }

    public void addProduto(Produto produto){
        produtos.add(produto);
    }

    public int getId(int id) {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public CLiente getNome() {
        return nome;
    }

    public void setNome(CLiente nome) {
        this.nome = nome;
    }

    public Endereco getEnderecoEntrega() {
        return enderecoEntrega;
    }

    public void setEnderecoEntrega(Endereco enderecoEntrega) {
        this.enderecoEntrega = enderecoEntrega;
    }

    public StatusPedido getStatus() {
        return status;
    }

    public void setStatus(StatusPedido status) {
        this.status = status;
    }

    public double valorTotal(){
        double soma = 0;
        for (Produto produto : produtos){
            soma = soma + produto.getPreco();
        }
        return soma;
    }

    public String toString() {
        return
                "id = " + id +
                "\n | nome = " + nome +
                "\n | produtos = " + produtos +
                "\n | enderecoEntrega = " + enderecoEntrega +
                "\n | status = " + status;
    }


}
