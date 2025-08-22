package exPF.exercicioPorFora.Controller;

import exPF.exercicioPorFora.Model.ProdutoModel;
import exPF.exercicioPorFora.Repostory.ProdutoRepository;
import exPF.exercicioPorFora.Service.ProdutoService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RequiredArgsConstructor
@RestController
@RequestMapping("/produtos")
public class ProdutoController {

    private final ProdutoService produtoService;

    @PostMapping("/salvar")
    public ProdutoModel salvar(@RequestBody ProdutoModel produtoModel){
        return produtoService.salvar(produtoModel);
    }

    @GetMapping("{id}")
    public ProdutoModel buscar(@PathVariable("id") Integer id){
        return produtoService.buscarPorId(id);
    }

    @DeleteMapping("{id}")
    public void deletar(@PathVariable("id") String id){
        produtoService.
    }

}
