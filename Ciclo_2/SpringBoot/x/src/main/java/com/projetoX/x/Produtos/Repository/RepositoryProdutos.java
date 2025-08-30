package com.projetoX.x.Produtos.Repository;

import com.projetoX.x.Produtos.Model.ModelProdutos;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface RepositoryProdutos extends JpaRepository<ModelProdutos, Integer> {
    List<ModelProdutos> findByNome(String nomeProduto);

}
