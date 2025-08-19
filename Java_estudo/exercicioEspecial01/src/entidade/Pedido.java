package entidade;

import java.util.ArrayList;
import java.util.List;

public class Pedido {
    private int id;
    private Cliente cliente;
    private List<Produto> produto = new ArrayList<>();
    private Endereco enderecoEntrega;
    private Status status;

    public Pedido(int id, Cliente cliente, Endereco enderecoEntrega,Status status) {
        this.id = id;
        this.cliente = cliente;
        this.produto = produto;
        this.enderecoEntrega = enderecoEntrega;
        this.status = status;
    }

    public Status getStatus() {
        return status;
    }

    public void setStatus(Status status) {
        this.status = status;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }




    public Endereco getEnderecoEntrega() {
        return enderecoEntrega;
    }

    public void setEnderecoEntrega(Endereco enderecoEntrega) {
        this.enderecoEntrega = enderecoEntrega;
    }
    public void adicionarProduto(Produto produto ){
        this.produto.add(produto);

    }
    public double valorTotal() {
        double total = 0.0;
        if (produto != null) {
            for (Produto p : produto) {
                total += p.getPreco();
            }
        }
        return total;
    }

    @Override
    public String toString() {
        return "Pedido{" +
                "id=" + id +
                "produto" + produto +
                ", cliente=" + cliente.getNome() +
                ", enderecoEntrega=" + enderecoEntrega +
                ", status=" + status +
                '}';
    }
}
