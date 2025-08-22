package exPF.exercicioPorFora.Service;


import exPF.exercicioPorFora.Model.ProdutoModel;
import exPF.exercicioPorFora.Repostory.ProdutoRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;


@Service
public class ProdutoService {
    private ProdutoRepository repository;

    public ProdutoService(ProdutoRepository repository) {
        this.repository = repository;
    }

    public ProdutoModel salvar(ProdutoModel novoProduto){
        novoProduto.setDateCriacao(LocalDate.now());
        return repository.save(novoProduto);
    }

    public ProdutoModel buscarPorId(Integer id){
        return repository.findById(id).orElse(null);
    }
}

