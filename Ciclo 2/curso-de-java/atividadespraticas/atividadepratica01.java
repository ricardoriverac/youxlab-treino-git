package atividadespraticas;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class atividadepratica01 {
    public static void main(String[] args) {
        BufferedReader dadEnt = new BufferedReader(new InputStreamReader(System.in));
        String p1 = "";
        String p2 = "";
        String p3 = "";
        String p4 = "";
        String p5 = "";
        System.out.println("Fale a 1ra palavra: ");
        try {
            p1 = dadEnt.readLine();
        } catch (IOException ex){
                ex.printStackTrace();
          };
        System.out.println("Fale a 2da palavra: ");
        try {
            p2 = dadEnt.readLine();
        } catch (IOException ex){
            ex.printStackTrace();
        };
        System.out.println("Fale a 3ra palavra: ");
        try {
            p3 = dadEnt.readLine();
        } catch (IOException ex){
            ex.printStackTrace();
        };
        System.out.println("Fale a 4ta palavra: ");
        try {
            p4 = dadEnt.readLine();
        } catch (IOException ex){
            ex.printStackTrace();
        };
        System.out.println("Fale a 5ta palavra: ");
        try {
            p5 = dadEnt.readLine();
        } catch (IOException ex){
            ex.printStackTrace();
        };


        System.out.println("palavra 1 : " + p1 + ", palavra 2 :" + p2 + ", palavra 3: " + p3 + ", palavra 4: " + p4 + ", palavra 5: " + p5 );






    }
}