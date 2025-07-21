package ProblemaExemplo.ultil;

public class aula81_ultil {
    private int number;
    private String holder;
    private double balance;

    public aula81_ultil(int number, String holder) {
        this.number = number;
        this.holder = holder;
    }

    public aula81_ultil(int number, String holder, double initialDeposit) {
        this.number = number;
        this.holder = holder;
        deposit(initialDeposit);
    }

    public String getHolder() {
        return holder;
    }

    public void setHolder(String holder) {
        this.holder = holder;
    }

    public double getBalance() {
        return balance;
    }

    public int getNumber() {
        return number;
    }

    public void deposit(double amount){
        balance += amount;
    }

    public void withdraw(double amount){
        balance -= amount + 5.0;
    }

    public String toString(){
        return "Account "
        + number
        + ", holder: "
        + holder
        + ", balance: $"
        + String.format("%.2f", balance);
    }


}
