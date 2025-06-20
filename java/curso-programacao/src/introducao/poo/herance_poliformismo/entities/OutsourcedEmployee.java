package introducao.poo.herance_poliformismo.entities;

public class OutsourcedEmployee extends Employee{
        private Double addtionalCharge;

    public OutsourcedEmployee(){
    }


    public OutsourcedEmployee(String name, Integer hours, Double valuePerHour , Double addtionalCharge) {
        super(name, hours, valuePerHour);
        this.addtionalCharge = addtionalCharge;
    }

    @Override
    public double payment(){
        return hours * valuePerHour + (addtionalCharge * 1.1);
    }

}
