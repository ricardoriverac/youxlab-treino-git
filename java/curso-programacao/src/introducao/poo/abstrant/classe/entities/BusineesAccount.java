package introducao.poo.abstrant.classe.entities;

// BusinessAccount e uma subclasse(Classe derivada) de account (Classe Base/Super Classe)significa ,
// então ela pode herdar os atribuito da outra classe

public class BusineesAccount extends Account {
    private Double loanLimit;

    public BusineesAccount(){
        super();
    }

    public BusineesAccount(Integer number, String holder, Double balance, Double loanLimit) {
        // Para executar o Construtor da classe base

        super(number, holder, balance);
        this.loanLimit = loanLimit;
    }

    public Double getLoanLimit() {
        return loanLimit;
    }

    public void setLoanLimit(Double loanLimit) {
        this.loanLimit = loanLimit;
    }

    public void loan(double amount){
        if (amount <= loanLimit){
            balance += amount - 10.0;
        }
    }
    @Override
    public void withdraw(double amount){
        super.withdraw(amount);
        balance -= 2.0;
    }
}

