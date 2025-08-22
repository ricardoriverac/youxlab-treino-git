package exPF.exercicioPorFora.Repostory;

import exPF.exercicioPorFora.Model.ProdutoModel;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ProdutoRepository extends JpaRepository<ProdutoModel, Integer> {
    List<ProdutoModel> findByProduto(String produto);
}
