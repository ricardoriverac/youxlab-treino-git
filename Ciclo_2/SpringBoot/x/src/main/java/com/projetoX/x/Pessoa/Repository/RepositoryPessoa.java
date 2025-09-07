package com.projetoX.x.Pessoa.Repository;

import com.projetoX.x.Pessoa.Model.ModelPessoa;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;
import java.util.Optional;

public interface RepositoryPessoa extends JpaRepository<ModelPessoa, Integer> {
    List<ModelPessoa> findByNome(String nomePessoa);

    Optional<ModelPessoa> findByEmail(String email);
}