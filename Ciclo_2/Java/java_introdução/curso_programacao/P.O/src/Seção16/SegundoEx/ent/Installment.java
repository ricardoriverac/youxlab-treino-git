package Seção16.SegundoEx.ent;

import java.time.LocalDate;

public class Installment {

    private LocalDate date;

    @Override
    public String toString() {
        return date + " -- " + String.format("%.2f", amount);
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    private double amount;

    public Installment(LocalDate date, double amount) {
        this.date = date;
        this.amount = amount;
    }

    public LocalDate getDate(){
        return date;
    }

}
