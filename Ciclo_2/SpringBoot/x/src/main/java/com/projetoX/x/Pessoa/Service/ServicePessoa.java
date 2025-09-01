package com.projetoX.x.Pessoa.Service;

import com.projetoX.x.Pessoa.Model.ModelPessoa;
import com.projetoX.x.Pessoa.Repository.RepositoryPessoa;
import org.springframework.stereotype.Component;

@Component
public class ServicePessoa {

    private RepositoryPessoa repository;

    public ServicePessoa(RepositoryPessoa repository) {
        this.repository = repository;
    }

    public ModelPessoa salvar(ModelPessoa novaPessoa){
        return repository.save(novaPessoa);
    }

    public ModelPessoa buscarPorId(Integer id){
        return repository.findById(id).orElse(null);
    }

    public void deletarPorId(Integer id){
        repository.deleteById(id);
    }

    public void atualizarPessoa(ModelPessoa pessoa){
        repository.save(pessoa);
    }
}
