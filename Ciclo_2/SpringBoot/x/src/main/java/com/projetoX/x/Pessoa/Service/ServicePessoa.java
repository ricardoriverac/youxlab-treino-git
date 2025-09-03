package com.projetoX.x.Pessoa.Service;

import com.projetoX.x.Pessoa.Model.ModelPessoa;
import com.projetoX.x.Pessoa.Repository.RepositoryPessoa;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
@RequiredArgsConstructor
public class ServicePessoa {

    private final RepositoryPessoa repository;
    private final PasswordEncoder passwordEncoder;

    public ModelPessoa salvar(ModelPessoa novaPessoa) {
        novaPessoa.setSenha(passwordEncoder.encode(novaPessoa.getSenha()));
        return repository.save(novaPessoa);
    }

    public ModelPessoa buscarPorId(Integer id) {
        return repository.findById(id).orElse(null);
    }

    public void deletarPorId(Integer id) {
        repository.deleteById(id);
    }

    public void atualizarPessoa(ModelPessoa pessoa) {
        repository.save(pessoa);
    }

    public boolean login(String email, String senhaDigitada) {
        Optional<ModelPessoa> optionalUsuario = repository.findByEmail(email);

        if (optionalUsuario.isPresent()) {
            ModelPessoa usuario = optionalUsuario.get();

            return passwordEncoder.matches(senhaDigitada, usuario.getSenha());
        }

        return false;
    }
}