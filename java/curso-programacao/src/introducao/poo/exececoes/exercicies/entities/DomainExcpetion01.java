package introducao.poo.exececoes.exercicies.entities;

import java.io.Serial;

public class DomainExcpetion01 extends RuntimeException {
  @Serial
  private static final long serialVersionUID = 1L;
  public DomainExcpetion01(String message) {
        super(message);
    }
}
