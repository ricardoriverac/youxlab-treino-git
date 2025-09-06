package davisales07.com.github.daviyoux01.repository;

import davisales07.com.github.daviyoux01.model.Produto;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ProdutoRepository extends JpaRepository<Produto, String> {

List<Produto> findByNome(String nome);

}
