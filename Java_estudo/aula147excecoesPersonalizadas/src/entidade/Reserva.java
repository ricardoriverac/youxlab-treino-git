package entidade;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class Reserva {
    private Integer numeroQuarto;
    private Date checkIn;
    private Date checkOut;

    private static SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

    public Reserva(Integer numeroQuarto, Date checkIn, Date checkOut) {
        numeroQuarto = numeroQuarto;
        this.checkIn = checkIn;
        this.checkOut = checkOut;
    }

    public Integer getnumeroQuarto() {
        return numeroQuarto;
    }

    public void setnumeroQuarto(Integer numeroQuarto) {
        numeroQuarto = numeroQuarto;
    }

    public Date getCheckIn() {
        return checkIn;
    }

    public Date getCheckOut() {
        return checkOut;
    }
    public long duration(){
        long diferencaDatas = checkOut.getTime() - checkIn.getTime();
        return TimeUnit.DAYS.convert(diferencaDatas,TimeUnit.MILLISECONDS);
    }
    public void updateDates(Date checkIn,Date checkOut) {
        this.checkIn = checkIn;
        this.checkOut = checkOut;
    }

    @Override
    public String toString(){
        return "Numero quarto"
                + numeroQuarto
                + ", check-in: "
                + sdf.format(checkIn)
                + " , check-out: "
                + sdf.format(checkOut)
                + ", "
                + duration()
                + "noites ";

    }
}
