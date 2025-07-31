package com.youxlab.cursodespring.applicacaospring.Repository;

import com.youxlab.cursodespring.applicacaospring.Model.ProdutoModel;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ProdutoRepository extends JpaRepository<ProdutoModel, String> {
    List<ProdutoModel> findByNome(String nome);
}
