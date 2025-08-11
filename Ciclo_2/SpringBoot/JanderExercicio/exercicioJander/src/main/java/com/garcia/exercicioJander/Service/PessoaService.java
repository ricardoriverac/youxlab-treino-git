package com.garcia.exercicioJander.Service;

import com.garcia.exercicioJander.Model.PessoaModel;
import com.garcia.exercicioJander.Repository.PessoaRepository;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

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

    public List<PessoaModel> filtroCidade(String cidade) {
        List<PessoaModel> pessoas = pessoaRepository.findAll();
        return pessoas.stream().filter(x -> x.getCidade().equals(cidade)).toList();
    }

    public List<PessoaModel> filtro30() {
        List<PessoaModel> pessoas = pessoaRepository.findAll();
        for (PessoaModel pessoa : pessoas) {
            pessoa.setNome(pessoa.getNome().toUpperCase());
        }
        return pessoas.stream().filter(x -> x.getIdade() > 30).toList();
    }

    public PessoaModel maisVelha() {
        List<PessoaModel> pessoas = pessoaRepository.findAll();

        PessoaModel pessoaModel = new PessoaModel();

        for (PessoaModel pessoa : pessoas) {
            if (pessoa.getIdade() > pessoaModel.getIdade()) {
                pessoaModel = pessoa;
            }
        }
        return pessoaModel;
    }

    public Map<String, Long> cpc() {
        List<PessoaModel> pessoas = pessoaRepository.findAll();

        Map<String, Long> contagem = new HashMap<>();
        for (PessoaModel pessoa : pessoas) {
            contagem.put(pessoa.getCidade(), contagem.getOrDefault(pessoa.getCidade(), 0L) + 1);
        }
        return contagem;
    }

    public boolean tdsMaiores() {
        List<PessoaModel> pessoas = pessoaRepository.findAll();
        if (pessoas.stream().filter(x -> x.getIdade() > 18).isParallel()) {
            return true;
        } else {
            return false;
        }
    }

    public double mediaC(String cidade){
        List<PessoaModel> pessoas = pessoaRepository.findAll();

        int count = 0;
        double media = 0;

        for (PessoaModel pessoa : pessoas){
            if (pessoa.getCidade().equals(cidade)){
                media += pessoa.getIdade();
                count += 1;
            }
        }
        media = media/count;
        return media;
    }
}
