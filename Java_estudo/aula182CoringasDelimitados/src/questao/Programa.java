package questao;

import entidades.Circle;
import entidades.Rectangle;
import entidades.Shape;

import java.util.ArrayList;
import java.util.List;

public class Programa {
    public static void main(String[] args) {
        List<Shape> myShape = new ArrayList<>();
        myShape.add(new Rectangle(3.0,2.0));
        myShape.add(new Circle(2.0));

        List<Circle> myCircles = new ArrayList<>();
        myCircles.add(new Circle(2.0));
        myCircles.add(new Circle(3.0));

        System.out.println("Total area: " + totalArea(myShape));
    }
    public static double totalArea(List<Shape>list){
        double sum = 0.0;
        for (Shape s : list){
            sum += s.area();
        }
        return sum;
    }

}
