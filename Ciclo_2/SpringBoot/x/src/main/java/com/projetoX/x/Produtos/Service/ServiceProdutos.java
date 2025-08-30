package com.projetoX.x.Produtos.Service;

import com.projetoX.x.Produtos.Model.ModelProdutos;
import com.projetoX.x.Produtos.Repository.RepositoryProdutos;
import org.springframework.stereotype.Component;

@Component
public class ServiceProdutos {
    private RepositoryProdutos repository;

    public ServiceProdutos(RepositoryProdutos repositoryProdutos) {
        this.repository = repositoryProdutos;
    }

    public ModelProdutos salvar(ModelProdutos novosProduto){
        return repository.save(novosProduto);
    }
}
