package Seção14.ExceçõesPersonalizadas.Entities;

import java.util.Date;

public class Reservation {

    private Integer roomNumber;
    private Date chekIn;
    private Date chekOut;

    public Reservation(Integer roomNumber, Date chekIn, Date chekOut) {
        super();
        this.roomNumber = roomNumber;
        this.chekIn = chekIn;
        this.chekOut = chekOut;
    }
}
