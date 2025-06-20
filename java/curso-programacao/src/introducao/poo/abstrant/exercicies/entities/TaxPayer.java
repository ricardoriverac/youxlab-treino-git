package introducao.poo.abstrant.exercicies.entities;

public abstract class TaxPayer {
    private String name;
    private Double anuallincome;

    public TaxPayer() {
    }

    public TaxPayer(String name, Double anuallincome) {
        this.name = name;
        this.anuallincome = anuallincome;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getAnuallincome() {
        return anuallincome;
    }

    public void setAnuallincome(Double anuallincome) {
        this.anuallincome = anuallincome;
    }

    public abstract double tax();
}