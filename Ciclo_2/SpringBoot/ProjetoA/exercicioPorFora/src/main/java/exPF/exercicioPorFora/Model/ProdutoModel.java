package exPF.exercicioPorFora.Model;

import exPF.exercicioPorFora.Model.Enum.StatusProduto;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import java.time.LocalDate;

@Entity
@Table(name = "Produto")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@EntityListeners(AuditingEntityListener.class)
public class ProdutoModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    private String produto;
    private String descricao;

    @Enumerated(EnumType.STRING)
    private StatusProduto status;

    @CreatedDate
    @Column(name = "data_criacao")
    private LocalDate dateCriacao;
}
