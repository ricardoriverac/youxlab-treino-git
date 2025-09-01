package com.projetoX.x.Produtos.Controller;

import com.projetoX.x.Produtos.Model.ModelProdutos;
import com.projetoX.x.Produtos.Service.ServiceProdutos;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RequiredArgsConstructor
@RestController
@RequestMapping("/produtosX")
public class ControllerProdutos {

    private final ServiceProdutos serviceProdutos;

    @PostMapping("/salvar")
    public ModelProdutos salvar(@RequestBody ModelProdutos modelProdutos){
        return serviceProdutos.salvar(modelProdutos);
    }

    @GetMapping("/buscar/{id}")
    public ModelProdutos buscar(@PathVariable("id") Integer id){
        return serviceProdutos.buscarPorId(id);
    }

    @DeleteMapping("deletar/{id}")
    public void deletar(@PathVariable("id") Integer id){
        serviceProdutos.deletarPorId(id);
    }

    @PutMapping("/atualizar/{id}")
    public void atualizarProdutos(@PathVariable("id") Integer id, @RequestBody ModelProdutos produtos){
        produtos.setId(id);
        serviceProdutos.atualizarProduto(produtos);
    }
}
