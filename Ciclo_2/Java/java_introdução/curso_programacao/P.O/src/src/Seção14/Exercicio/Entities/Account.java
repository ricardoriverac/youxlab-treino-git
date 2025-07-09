package Seção14.Exercicio.Entities;

public class Account {

    private Integer number;
    private String holder;
    private double balance;
    private double withdrawLimit;

    public Account(Integer number, String holder, double balance, double withdrawLimit) {
        this.number = number;
        this.holder = holder;
        this.balance = balance;
        this.withdrawLimit = withdrawLimit;
    }

    public Account() {

    }

    public void deposit(double amount) {
        balance += amount;
    }

    public Integer getNumber() {
        return number;
    }

    public void setNumber(Integer number) {
        this.number = number;
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

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public double getWithdrawLimit() {
        return withdrawLimit;
    }

    public void setWithdrawLimit(double withdrawLimit) {
        this.withdrawLimit = withdrawLimit;
    }

    public void withdraw(double amount, double withdrawLimit, double balance) {
        if (amount > withdrawLimit ){
            System.out.println("Uai paizão, seu limite é: " + withdrawLimit + ", vamo pegar leve né");
        }
        else {
            balance -= amount;
            System.out.println("Saque efetuado com sucesso!\nSeu saldo: " + balance);
        }
    }






}
