package introducao.poo.interfaces.model.model.heloo.services;

import introducao.poo.interfaces.model.entities.Carrental;
import introducao.poo.interfaces.model.model.heloo.entities.Invoice;

import java.time.Duration;

public class RentalService {
    private double pricePerday;
    private double pricePerhour;

    private TaxService taxService;

    public RentalService(double pricePerday, double pricePerhour, BrazilTaxService taxService) {
        this.pricePerday = pricePerday;
        this.pricePerhour = pricePerhour;
        this.taxService = taxService;
    }

    public void processInvoce(Carrental carRental){

        double minus = Duration.between(carRental.getStart(), carRental.getFinish()).toMinutes();

        double hours = minus / 60.0;

        double basicPayment;
        if (hours <= 12){
            basicPayment = pricePerhour * Math.ceil(hours);
        }
        else {
            basicPayment = pricePerday * Math.ceil(hours / 24.0);
        }
        double tax = taxService.tax(basicPayment);
        carRental.setInvoice(new Invoice(basicPayment , tax));
    }
}
