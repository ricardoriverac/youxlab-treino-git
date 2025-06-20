package introducao.poo.abstrant.metedo.aplication;

import introducao.poo.abstrant.metedo.entities.Color;
import introducao.poo.abstrant.metedo.entities.Circule;
import introducao.poo.abstrant.metedo.entities.Retangule;
import introducao.poo.abstrant.metedo.entities.Shape;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class aplicationShape {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the numbers of shapes");
        int quant = input.nextInt();

        List<Shape> shapes = new ArrayList<>();

        for (int i = 0; i < quant; i++) {
            System.out.printf("Enter the #%d data %n" , (i+1));
            System.out.print("Rectangle or circule (r/c)? ");
            char ch = input.next().charAt(0);
            System.out.print("Color (BLACK/BLUE/RED): ");
            Color color = Color.valueOf(input.next());
            if (ch == 'r'){
                System.out.print("Width: ");
                double width = input.nextDouble();
                System.out.print("Height: ");
                double height = input.nextDouble();
                shapes.add(new Retangule(color , width , height));
            }
            else {
                System.out.print("Radius: ");
                double radius = input.nextDouble();
                shapes.add(new Circule(color , radius));
            }
        }
        System.out.println();
        System.out.println("SHAPES AREAS");
        for (Shape shape : shapes) {
            System.out.printf("%.2f" , shape.area());
        }


    }
}
