package Seção14.ExceçõesPersonalizadas.Entities;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class ReservationR {

    private Integer roomNumber;
    private Date chekIn;
    private Date chekOut;

    private static SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

    public ReservationR(Integer roomNumber, Date chekIn, Date chekOut) {
        super();
        this.roomNumber = roomNumber;
        this.chekIn = chekIn;
        this.chekOut = chekOut;
    }

    public Integer getRoomNumber() {
        return roomNumber;
    }

    public void setRoomNumber(Integer roomNumber) {
        this.roomNumber = roomNumber;
    }

    public Date getChekIn() {
        return chekIn;
    }

    public Date getChekOut() {
        return chekOut;
    }

    public long duration(){
        long diff = chekOut.getTime() - chekIn.getTime();
        return TimeUnit.DAYS.convert(diff, TimeUnit.MILLISECONDS);
    }

    public String updatesDates(Date chekIn, Date chekOut){

        Date now = new Date();
        if (chekIn.before(now) || chekOut.before(now)){
            return "Error in reservation: Reservation dates for update must be future";
        }
        if (!chekOut.after(chekIn)) {
            return "Error in reservation: Check-out date must be after check-in date";
        }

        this.chekIn = chekIn;
        this.chekOut = chekOut;

        return null;
    }

    @Override
    public String toString() {
        return "Room "
                + roomNumber
                + ", chekIn: "
                + sdf.format(chekIn)
                + ", chekOut: "
                + sdf.format(chekOut)
                + ", "
                + duration()
                +" nights";
    }
}
