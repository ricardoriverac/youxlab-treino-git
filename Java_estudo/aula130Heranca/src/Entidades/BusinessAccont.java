package Entidades;

public class BusinessAccont extends Account {
    private Double loanLimit;

    public BusinessAccont() {
        super();
    }

    public BusinessAccont(Integer number, String holder, Double balance, Double loanLimit) {
        super(number, holder, balance);
        this.loanLimit = loanLimit;
    }

    public Double getLoanLimit() {
        return loanLimit;
    }

    public void setLoanLimit(Double loanLimit) {
        this.loanLimit = loanLimit;
    }

    public void loan(double amount) {
        if (amount <= loanLimit) {
            balance += amount - 10.0;

        }
    }

    @Override
    public void withdraw(double amount) {
        super.withdraw(amount);
        balance -= 2.0;
    }

}
