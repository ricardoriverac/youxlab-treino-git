package introducao.poo.abstrant.exercicies.entities;

public class Individual extends TaxPayer{

    private Double heathexpenditures;

    public Individual(){
    }

    public Individual(String name, Double anuallincome, Double heathexpenditures) {
        super(name, anuallincome);
        this.heathexpenditures = heathexpenditures;
    }

    public Double getHeathexpenditures() {
        return heathexpenditures;
    }

    public void setHeathexpenditures(Double heathexpenditures) {
        this.heathexpenditures = heathexpenditures;
    }

    @Override
    public double tax() {
        double basicTax;
        if (getAnuallincome() < 20000.0){
            basicTax = getAnuallincome() * 0.15;
        }
        else {
            basicTax = getAnuallincome() * 0.25;
        }
        basicTax = basicTax - (getHeathexpenditures() * 0.5);
        return basicTax;
    }
}
