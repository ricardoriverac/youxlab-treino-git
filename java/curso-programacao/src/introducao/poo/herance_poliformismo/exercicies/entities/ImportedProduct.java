package introducao.poo.herance_poliformismo.exercicies.entities;

public class ImportedProduct extends Product{

    private Double custonsFee;

    public ImportedProduct(){

    }

    public ImportedProduct(String name, Double price, Double custonsFee) {
        super(name, price);
        this.custonsFee = custonsFee;
    }

    public Double getCustonsFee() {
        return custonsFee;
    }

    public void setCustonsFee(Double custonsFee) {
        this.custonsFee = custonsFee;
    }

    @Override
    public String toString(){
        return name + " " + price + " (CustonsFee: $ " + String.format("%.2f" , custonsFee) + ")";
    }

    public double totalPrice(double custonsFee){
        return price += custonsFee;
    }
}
