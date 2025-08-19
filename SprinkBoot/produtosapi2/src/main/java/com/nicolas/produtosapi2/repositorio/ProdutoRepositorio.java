package com.nicolas.produtosapi2.repositorio;

import com.nicolas.produtosapi2.model.Produto;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ProdutoRepositorio extends JpaRepository <Produto,String> {
    List<Produto> findByNome(String nome);
}



