package ProblemaExemplo.entities;

public class AlturaEnt {

    private String name;
    private int age;
    private double heigth;

    public AlturaEnt(String name, int age, double heigth) {
        this.name = name;
        this.age = age;
        this.heigth = heigth;
    }

    public String getName() {
        return name;
    }

    public double getHeigth() {
        return heigth;
    }

    public int getAge() {
        return age;
    }
}
