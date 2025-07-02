package introducao.poo.interfaces.entities.model.entities;

import introducao.poo.interfaces.entities.model.services.Veiculo;

import java.time.LocalDateTime;

public class Carrental {
    private LocalDateTime start;
    private LocalDateTime finish;
    private Veiculo veiculo;
    private Invoice invoice;

    public Carrental(LocalDateTime start, LocalDateTime finish, Veiculo veiculo, Invoice invoice) {
        this.start = start;
        this.finish = finish;
        this.veiculo = veiculo;
        this.invoice = invoice;
    }

    public LocalDateTime getStart() {
        return start;
    }

    public void setStart(LocalDateTime start) {
        this.start = start;
    }

    public LocalDateTime getFinish() {
        return finish;
    }

    public void setFinish(LocalDateTime finish) {
        this.finish = finish;
    }

    public Invoice getInvoice() {
        return invoice;
    }

    public void setInvoice(Invoice invoice) {
        this.invoice = invoice;
    }

    public Veiculo getVeiculo() {
        return veiculo;
    }

    public void setVeiculo(Veiculo veiculo) {
        this.veiculo = veiculo;
    }
}
