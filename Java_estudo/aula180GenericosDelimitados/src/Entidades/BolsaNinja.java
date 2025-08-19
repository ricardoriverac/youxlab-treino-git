package Entidades;

// BolsaNinja.java
import java.util.ArrayList;
import java.util.List;

public class BolsaNinja<T extends Ferramentas> {
    private List<T> ferramentas = new ArrayList<>();

    public void adicionarFerramenta(T ferramenta) {
        ferramentas.add(ferramenta);
    }

    public void mostrarNomes() {
        for (T f : ferramentas) {
            System.out.println("Nome da ferramenta: " + f.getNome());
        }
    }
}

