package Seção16.SegundoEx.ent;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Contract {

    private Integer number;
    private LocalDate date;
    private double totalValue;

    private List<Installment> installments = new ArrayList<>();

    public Contract() {

    }

    public Contract(int number, LocalDate date, double totalValue) {
    }

    public Integer getNumber() {
        return number;
    }

    public void setNumber(Integer number) {
        this.number = number;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public double getTotalValue() {
        return totalValue;
    }

    public void setTotalValue(double totalValue) {
        this.totalValue = totalValue;
    }

    public List<Installment> getInstallments() {
        return installments;
    }

    public void setInstallments(List<Installment> installments) {
        this.installments = installments;
    }

    public Contract(Integer number, LocalDate date, double totalValue, List<Installment> installments) {
        this.number = number;
        this.date = date;
        this.totalValue = totalValue;
        this.installments = installments;
    }
}
