package Seção16.PrimeiroEx.Model.service;

import Seção16.PrimeiroEx.Ent.CarRental;
import Seção16.PrimeiroEx.Ent.Invoice;

import java.time.Duration;

public class RentalService {

    private Double pricePerHour;
    private Double pricePerDay;

    private BrazilTaxService taxService;

    public RentalService(Double pricePerHour, Double pricePerDay, BrazilTaxService taxService) {
        this.pricePerHour = pricePerHour;
        this.pricePerDay = pricePerDay;
        this.taxService = taxService;
    }

    public void processInvoice(CarRental carRental){

       double minutes =  Duration.between(carRental.getStart(), carRental.getFinish()).toMinutes();
       double hours = minutes / 60;

       carRental.setInvoice(new Invoice(50.0, 10.0));

    }

}
