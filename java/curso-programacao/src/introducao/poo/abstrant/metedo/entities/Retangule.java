package introducao.poo.abstrant.metedo.entities;


// Para que uma subclasse não se torne abstrata faça com que o método da super classe seja abstrato no caso chame
// chame ele na subclasse
public class Retangule extends Shape{
    private Double widgt;
    private Double heigth;

    public Retangule(){

    }

    public Retangule(Color color, Double widgt, Double heigth) {
        super(color);
        this.widgt = widgt;
        this.heigth = heigth;
    }

    public Double getWidgt() {
        return widgt;
    }

    public void setWidgt(Double widgt) {
        this.widgt = widgt;
    }

    public Double getHeigth() {
        return heigth;
    }

    public void setHeigth(Double heigth) {
        this.heigth = heigth;
    }

    @Override
    public double area() {
        return widgt * heigth;
    }
}
