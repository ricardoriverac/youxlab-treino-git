package introducao.poo.abstrant.metedo.entities;

public class Circule extends Shape{

    private final int expoencia = 1;

    private Double radius;

    public Circule(){

    }

    public Circule(Color color, Double radius) {
        super(color);
        this.radius = radius;
    }


    public void setRadius(Double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}
