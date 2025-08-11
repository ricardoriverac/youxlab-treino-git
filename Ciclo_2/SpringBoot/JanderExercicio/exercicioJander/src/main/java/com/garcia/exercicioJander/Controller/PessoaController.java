package com.garcia.exercicioJander.Controller;

import com.garcia.exercicioJander.Model.PessoaModel;
import com.garcia.exercicioJander.Repository.PessoaRepository;
import com.garcia.exercicioJander.Service.PessoaService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RequiredArgsConstructor
@RestController
@RequestMapping("/pessoas")
public class PessoaController {

    private final PessoaRepository pessoaRepository;
    private final PessoaService pessoaService;

    @PostMapping("/cadastrar")
    public PessoaModel cadastrar(@RequestBody PessoaModel pessoaModel) {
        System.out.println("Pessoa salva com sucesso: " + pessoaModel);
        pessoaRepository.save(pessoaModel);
        return pessoaModel;
    }

    @GetMapping("/maiores")
    public List<PessoaModel> maioresde18(@RequestParam("cidade") String cidade) {
        return pessoaService.filtro18(cidade);
    }

    @GetMapping("/por-cidade")
    public List<PessoaModel> porCidade(@RequestParam("cidade") String cidade) {
        return pessoaService.filtroCidade(cidade);
    }

    @GetMapping("/maiores-30-nomes")
    public List<PessoaModel> maioresde30() {
        return pessoaService.filtro30();
    }

    @GetMapping("/mais-velha")
    public PessoaModel maisVelha(){
        return pessoaService.maisVelha();
    }

    @GetMapping("/contagem-por-cidade")
    public Map<String, Long> cpc(){
        return pessoaService.cpc();
    }

    @GetMapping("/todas-maiores")
    public boolean tdsMaiores(){
        return pessoaService.tdsMaiores();
    }

    @GetMapping("/media-idade")
    public double mediaC(@RequestParam("cidade") String cidade){
        return pessoaService.mediaC(cidade);

    }

}