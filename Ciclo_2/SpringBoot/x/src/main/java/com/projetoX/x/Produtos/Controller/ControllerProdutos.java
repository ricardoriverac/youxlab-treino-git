package com.projetoX.x.Produtos.Controller;

import com.projetoX.x.Produtos.Model.ModelProdutos;
import com.projetoX.x.Produtos.Service.ServiceProdutos;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequiredArgsConstructor
@RestController
@RequestMapping("/produtosX")
public class ControllerProdutos {

    private final ServiceProdutos serviceProdutos;

    @PostMapping("/salvar")
    public ModelProdutos salvar(@RequestBody ModelProdutos modelProdutos){
        return serviceProdutos.salvar(modelProdutos);
    }
}
