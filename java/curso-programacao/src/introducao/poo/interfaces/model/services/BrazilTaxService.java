package introducao.poo.interfaces.model.model.heloo.services;

public class BrazilTaxService implements TaxService {
    public double tax(double amount){
        if (amount < 100.00){
            return amount * 0.2;
        }
        else {
            return amount * 0.15;
        }
    }
}
