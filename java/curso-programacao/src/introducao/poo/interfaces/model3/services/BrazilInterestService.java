package introducao.poo.interfaces.model3.entities;

import java.security.InvalidParameterException;

public class BrazilInterestService {
    private double interestRate;

    public BrazilInterestService(double interestRate) {
        this.interestRate = interestRate;
    }

    public double getInterestRate() {
        return interestRate;
    }
    public double payment(double amount , int months){
        if (months < 1){
            throw new InvalidParameterException("Months must be greater than zero");
        }
        return amount * Math.pow(1.0 + interestRate / 100 , months);
    }
}