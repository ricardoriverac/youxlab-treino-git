package introducao.java.funcoes;

import java.util.Scanner;

public class Funcoes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a;
        a = sc.nextInt();
        int b;
        b = sc.nextInt();
        int c;
        c = sc.nextInt();

        int height = max(a,b,c);

        showResult(height);
    }
    public static int max(int x, int y, int z){
        int aux;
        if(x > y){
            aux = x;
        }
        else if (y > z){
            aux = y;
        }
        else {
            aux = z;
        }
        return aux;
    }
    public static void showResult(int value){
        System.out.println("Height " + value);
    }
}
