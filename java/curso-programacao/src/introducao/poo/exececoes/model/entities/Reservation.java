package introducao.poo.exececoes.model.entities;


import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class Reservation {
    private Integer roomNumber;
    private Date checkin;
    private Date checkout;

    public Reservation(){

    }
    public Reservation(Integer roomNumber, Date checkin, Date checkout) throws DomainException {
        if (!checkout.after(checkin)) {
            throw new DomainException("Error in reservation: Check-out date must be after ckeck-in date");
        }
        this.roomNumber = roomNumber;
        this.checkin = checkin;
        this.checkout = checkout;
    }

    private static SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

    public Integer getRoomNumber() {
        return roomNumber;
    }

    public void setRoomNumber(Integer roomNumber) {
        this.roomNumber = roomNumber;
    }

    public Date getCheckin() {
        return checkin;
    }

    public Date getCheckout() {
        return checkout;
    }


    public long duration(){
        long diff = checkout.getTime() - checkin.getTime();
        return TimeUnit.DAYS.convert(diff, TimeUnit.MILLISECONDS);
    }
    public void updateDates(Date checkIn , Date checkOut) throws DomainException {
        Date now = new Date();
        if (checkIn.before(now) || checkOut.before(now)) {
            throw new DomainException("Error in reservation: Reservation dates for update must be future dates");
        }
        if (!checkOut.after(checkIn)) {
            throw new DomainException("Error in reservation: Check-out date must be after ckeck-in date");
        }
        this.checkin = checkIn;
        this.checkout = checkIn;
    }
    @Override
    public String toString(){
        return "Room "
                + roomNumber
                + ", checkin "
                + sdf.format(checkin)
                + ", "
                + duration()
                + "Nigths";

    }
}
