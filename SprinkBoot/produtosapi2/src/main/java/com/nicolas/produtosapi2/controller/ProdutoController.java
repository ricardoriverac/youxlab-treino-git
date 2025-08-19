package com.nicolas.produtosapi2.controller;

import com.nicolas.produtosapi2.model.Produto;
import com.nicolas.produtosapi2.repositorio.ProdutoRepositorio;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/produtos")
public class ProdutoController {

    private final ProdutoRepositorio produtoRepositorio;

    public ProdutoController(ProdutoRepositorio produtoRepositorio) {
        this.produtoRepositorio = produtoRepositorio;
    }

    @PostMapping
    public Produto salvar(@RequestBody Produto produto) {
        System.out.println("Produto recebido: " + produto);

        // Gerando um ID aleatório e setando no produto
        produto.setId(UUID.randomUUID().toString());

        produtoRepositorio.save(produto);
        return produto;
    }

    @GetMapping("{id}")
    public Produto obterPorid(@PathVariable String id) {
        return produtoRepositorio.findById(id).orElse(null);
    }

    @DeleteMapping("{id}")
    public void deletar(@PathVariable("id") String id) {
        produtoRepositorio.deleteById(id);
    }

    @PutMapping("{id}")
    public void atualizar(@PathVariable("id") String id,
                          @RequestBody Produto produto) {
        produto.setId(id);
        produtoRepositorio.save(produto);
    }
    @GetMapping
    public List<Produto> buscar(@RequestParam("nome") String nome){
       return produtoRepositorio.findByNome(nome);

    }
}
