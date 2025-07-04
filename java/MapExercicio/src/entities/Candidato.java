package entities;

import java.util.Objects;

public class Candidato {
    private String name;
    private Integer quantity;

    public Candidato(){}

    public Candidato(String name, Integer quantity) {
        this.name = name;
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getQuantity() {
        return quantity;
    }

    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Candidato candidato = (Candidato) o;
        return Objects.equals(name, candidato.name);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(name);
    }
}
