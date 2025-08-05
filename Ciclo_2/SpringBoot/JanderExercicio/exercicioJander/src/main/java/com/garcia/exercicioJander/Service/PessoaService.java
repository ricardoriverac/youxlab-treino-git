package com.garcia.exercicioJander.Service;

import com.garcia.exercicioJander.Model.PessoaModel;
import com.garcia.exercicioJander.Repository.PessoaRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PessoaService {

    private final PessoaRepository pessoaRepository;

    public PessoaService(PessoaRepository pessoaRepository) {
        this.pessoaRepository = pessoaRepository;
    }

    public List<PessoaModel> filtro18(String cidade) {
        List<PessoaModel> pessoas = pessoaRepository.findAll();

//        Stream<PessoaModel> stream = pessoas.stream();
//        Stream<PessoaModel> streamFiltrado = stream.filter(x -> x.getIdade() > 18 && x.getCidade().equals(cidade));
//        return streamFiltrado.toList();

        return pessoas.stream().filter(x -> x.getIdade() > 18 && x.getCidade().equals(cidade)).toList();
    }

    public List<PessoaModel> filtroCidade(String cidade){
        List<PessoaModel> pessoas = pessoaRepository.findAll();
        return pessoas.stream().filter(x -> x.getCidade().equals(cidade)).toList();
    }

    public List<PessoaModel> filtro30(){
        List<PessoaModel> pessoas = pessoaRepository.findAll();
        return pessoas.stream().filter(x -> x.getIdade() > 30).toList();
    }
}
