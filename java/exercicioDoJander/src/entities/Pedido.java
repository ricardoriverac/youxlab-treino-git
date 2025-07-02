package entities;

import enums.StaatusPedido;

import java.util.ArrayList;
import java.util.List;

public class Pedido {
    private Integer id;
    private Cliente cliente;
    private List<Produto> produtos = new ArrayList<>();

    private Endereco endereco;
    private StaatusPedido status;

    private Pedido(){}

    public Pedido(Integer id, Cliente cliente, Endereco endereco, StaatusPedido status) {
        this.id = id;
        this.cliente = cliente;
        this.endereco = endereco;
        this.status = status;
    }

    public double valorTotal(){
        double sum = 0.0;
        for (Produto produto : produtos) {
            sum = sum + produto.getPrice();
        }
        return sum;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public StaatusPedido getStatus() {
        return status;
    }

    public void setStatus(StaatusPedido status) {
        this.status = status;
    }

    public void addProduto(Produto produto){
        produtos.add(produto);
    }
}
