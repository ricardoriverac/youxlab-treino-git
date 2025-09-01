package com.projetoX.x.Produtos.Service;

import com.projetoX.x.Produtos.Model.ModelProdutos;
import com.projetoX.x.Produtos.Repository.RepositoryProdutos;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

@Service
public class ServiceProdutos {
    private RepositoryProdutos repository;

    public ServiceProdutos(RepositoryProdutos repositoryProdutos) {
        this.repository = repositoryProdutos;
    }

    public ModelProdutos salvar(ModelProdutos novosProduto){
        return repository.save(novosProduto);
    }

    public ModelProdutos buscarPorId(Integer id){
        return repository.findById(id).orElse(null);
    }

    public void deletarPorId(Integer id){
        repository.deleteById(id);
    }

    public void atualizarProduto(ModelProdutos produtos){
        repository.save(produtos);
    }
}
