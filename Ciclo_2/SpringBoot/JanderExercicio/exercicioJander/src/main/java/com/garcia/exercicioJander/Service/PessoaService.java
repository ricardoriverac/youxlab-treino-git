package com.garcia.exercicioJander.Service;

import com.garcia.exercicioJander.Model.PessoaModel;
import com.garcia.exercicioJander.Repository.PessoaRepository;
import org.springframework.stereotype.Service;

import java.util.*;

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

    public double mediaC(String cidade) {
        List<PessoaModel> pessoas = pessoaRepository.findAll();

        int count = 0;
        double media = 0;

        for (PessoaModel pessoa : pessoas) {
            if (pessoa.getCidade().equals(cidade)) {
                media += pessoa.getIdade();
                count += 1;
            }
        }
        media = media / count;
        return media;
    }

    public Map<String, Double> mpc() {
        List<PessoaModel> pessoas = pessoaRepository.findAll();

        Map<String, Integer> somaIdades = new HashMap<>();
        Map<String, Integer> contagem = new HashMap<>();

        for (PessoaModel p : pessoas) {
            String cidade = p.getCidade();
            int idade = p.getIdade();

            somaIdades.put(cidade, somaIdades.getOrDefault(cidade, 0) + idade);
            contagem.put(cidade, contagem.getOrDefault(cidade, 0) + 1);
        }

        Map<String, Double> mediaPorCidade = new HashMap<>();
        for (String cidade : somaIdades.keySet()) {
            double media = (double) somaIdades.get(cidade) / contagem.get(cidade);
            mediaPorCidade.put(cidade, media);
        }
        return mediaPorCidade;
    }

    public List<String> pca(){
        List<PessoaModel> pessoas = pessoaRepository.findAll();

        List<String> pessoasA = new ArrayList<>();

        for(PessoaModel pessoa : pessoas){
            if (pessoa.getNome().charAt(0) == 'A' || pessoa.getNome().charAt(0) == 'a'){
                pessoasA.add(pessoa.getNome());
            }
        }
        return pessoasA;
    }

    public List<String> nm(){
        List<PessoaModel> pessoas = pessoaRepository.findAll();

        Set<String> namesA = new HashSet<>();

        for (PessoaModel pesssoa : pessoas){
            namesA.add(pesssoa.getNome());
        }
        return namesA.stream().distinct().toList();
    }
}
