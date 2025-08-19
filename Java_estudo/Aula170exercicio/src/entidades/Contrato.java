package entidades;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class Contrato {
    private Integer numero;
    private LocalDate data;
    private Double totalValor;
    private List<Parcelas> parcelas = new ArrayList<>(); // minúscula e singular

    public Contrato() {
    }

    public Contrato(Integer numero, LocalDate data, Double totalValor) {
        this.numero = numero;
        this.data = data;
        this.totalValor = totalValor;
    }

    // Construtor que recebe LocalDateTime e converte para LocalDate
    public Contrato(Integer numero, LocalDateTime data, Double totalValor) {
        this.numero = numero;
        this.data = data.toLocalDate(); // converte para LocalDate
        this.totalValor = totalValor;
    }

    public Integer getNumero() {
        return numero;
    }

    public void setNumero(Integer numero) {
        this.numero = numero;
    }

    public LocalDate getData() {
        return data;
    }

    public void setData(LocalDate data) {
        this.data = data;
    }

    public Double getTotalValor() {
        return totalValor;
    }

    public void setTotalValor(Double totalValor) {
        this.totalValor = totalValor;
    }

    public List<Parcelas> getParcelas() {
        return parcelas;
    }
}
