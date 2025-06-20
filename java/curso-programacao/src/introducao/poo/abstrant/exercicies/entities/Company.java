package introducao.poo.abstrant.exercicies.entities;

public class Company extends TaxPayer{
    private Integer numberOfEmployees;

    public Company() {
    }

    public Company(String name, Double anuallincome, Integer numberOfEmployees) {
        super(name, anuallincome);
        this.numberOfEmployees = numberOfEmployees;
    }

    public Integer getNumberOfEmployees() {
        return numberOfEmployees;
    }

    public void setNumberOfEmployees(Integer numberOfEmployees) {
        this.numberOfEmployees = numberOfEmployees;
    }

    @Override
    public double tax() {
        if (numberOfEmployees > 10){
            return getAnuallincome() * 0.14;
        }
        else {
            return getAnuallincome() * 0.16;
        }
    }
}
