package com.youxlab.cursodespring.applicacaospring.Repository;

import com.youxlab.cursodespring.applicacaospring.Model.ProdutoModel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProdutoRepository extends JpaRepository<ProdutoModel, String> {
}
