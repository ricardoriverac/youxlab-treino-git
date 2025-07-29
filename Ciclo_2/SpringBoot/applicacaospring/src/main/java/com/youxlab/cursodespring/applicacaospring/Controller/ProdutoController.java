package com.youxlab.cursodespring.applicacaospring.Controller;

import com.youxlab.cursodespring.applicacaospring.Model.ProdutoModel;
import com.youxlab.cursodespring.applicacaospring.Repository.ProdutoRepository;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/produtos")
public class ProdutoController {

    private ProdutoRepository produtoRepository;

    public ProdutoController(ProdutoRepository produtoRepository) {
        this.produtoRepository = produtoRepository;
    }

    @PostMapping
    public ProdutoModel salvar(@RequestBody ProdutoModel produtoModel){
        System.out.println("Produto recebido: " + produtoModel);
        var id = UUID.randomUUID().toString();
        produtoModel.setId(id);
        produtoRepository.save(produtoModel);
        return produtoModel;
    }

    @GetMapping("/{id}")
    public ProdutoModel obterPorId(@PathVariable("id") String id){
        //Optional<ProdutoModel> produtoModel = produtoRepository.findById(id);
        //return produtoModel.isPresent() ? produtoModel.get() : null;

        return produtoRepository.findById(id).orElse(null);
    }

    @DeleteMapping("{id}")
    public void deletar(@PathVariable("id") String id){
        produtoRepository.deleteById(id);
    }

    @PutMapping("{id}")
    public void atualizar(@PathVariable("id") String id,
                          @RequestBody ProdutoModel produtoModel){
        produtoModel.setId(id);
        produtoRepository.save(produtoModel);
    }
}
