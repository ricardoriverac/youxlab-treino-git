package entidades;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Parcelas {
    private LocalDate dataVencimento;
    private Double valor;

    public Parcelas() {
    }

    public Parcelas(LocalDate dataVencimento, Double valor) {
        this.dataVencimento = dataVencimento;
        this.valor = valor;
    }

    public LocalDate getDataVencimento() {
        return dataVencimento;
    }

    public void setDataVencimento(LocalDate dataVencimento) {
        this.dataVencimento = dataVencimento;
    }

    public Double getValor() {
        return valor;
    }

    public void setValor(Double valor) {
        this.valor = valor;
    }

    @Override
    public String toString() {
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        return fmt.format(dataVencimento) + " - " + String.format("%.2f", valor);
    }

}
