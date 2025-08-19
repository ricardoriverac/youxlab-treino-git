package entidade;

import model.exceptions.DominioException;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class Reserva3 {
    private Integer numeroQuarto;
    private Date checkIn;
    private Date checkOut;

    private static SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

    public Reserva3(Integer numeroQuarto, Date checkIn, Date checkOut){
        Date agora = new Date();

        if (checkIn.before(agora) || checkOut.before(agora)) {
            throw new DominioException("sua mensagem aqui na exececao personalizada");
        }
        if (!checkOut.after(checkIn)) {
            throw new DominioException("Erro na reserva: check-out deve ser depois do check-in");
        }

        this.numeroQuarto = numeroQuarto;
        this.checkIn = checkIn;
        this.checkOut = checkOut;
    }

    public Integer getNumeroQuarto() {
        return numeroQuarto;
    }

    public void setNumeroQuarto(Integer numeroQuarto) {
        this.numeroQuarto = numeroQuarto;
    }

    public Date getCheckIn() {
        return checkIn;
    }

    public Date getCheckOut() {
        return checkOut;
    }

    public long duration() {
        long diferencaDatas = checkOut.getTime() - checkIn.getTime();
        return TimeUnit.DAYS.convert(diferencaDatas, TimeUnit.MILLISECONDS);
    }

    public void updateDates(Date checkIn, Date checkOut) {
        Date agora = new Date();

        if (checkIn.before(agora) || checkOut.before(agora)) {
            throw new IllegalArgumentException("Erro na reserva: as datas devem ser futuras");
        }
        if (!checkOut.after(checkIn)) {
            throw new IllegalArgumentException("Erro na reserva: check-out deve ser depois do check-in");
        }

        this.checkIn = checkIn;
        this.checkOut = checkOut;
    }

    @Override
    public String toString() {
        return "Número do quarto: "
                + numeroQuarto
                + ", check-in: "
                + sdf.format(checkIn)
                + ", check-out: "
                + sdf.format(checkOut)
                + ", "
                + duration()
                + " noites";
    }
}
