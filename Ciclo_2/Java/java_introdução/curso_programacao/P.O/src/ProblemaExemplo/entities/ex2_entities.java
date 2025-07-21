package ProblemaExemplo.entities;

public class ex2_entities {

    public String nome;
    public double grossSalary;
    public double tax;


    public double liquidSalary(){
        return grossSalary - tax;
    }

    public void increaseSalary(double porcentage){
        grossSalary += grossSalary * porcentage / 100.0;
    }

    public String toString(){
        return nome + ", $" + String.format("%.2f", liquidSalary());
    }

}
