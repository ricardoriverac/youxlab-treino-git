package com.projetoX.x.Pessoa.Repository;

import com.projetoX.x.Pessoa.Model.ModelPessoa;
import com.projetoX.x.Produtos.Model.ModelProdutos;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface RepositoryPessoa extends JpaRepository<ModelPessoa, Integer> {
    List<ModelPessoa> findByNome(String nomePessoa);
}
