package com.garcia.exercicioJander.Repository;

import com.garcia.exercicioJander.Model.PessoaModel;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface PessoaRepository extends JpaRepository<PessoaModel, String> {
    List<PessoaModel> findByNome(String nome);
}