package introducao.poo.exececoes.model.entities;


import java.io.Serial;

// RuntimeException: e aonde o compilador não obriga a você tratar a exceção
// Exception: o compilador obriga você a tratar aquela sessão
public class DomainException extends Exception {

    @Serial
    private static final long serialVersionUID = 1L;
    public DomainException(String message) {
        super(message);
    }
}
