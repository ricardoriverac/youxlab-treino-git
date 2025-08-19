package execucao;

import entidade.CLiente;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        CLiente c1 = new CLiente("Maria","maria@gmail.com ");
        CLiente c2 = new CLiente("Alex","alex@gmail.com");

        System.out.println(c1.hashCode());
        System.out.println(c2.hashCode());
        System.out.println(c1.equals(c2));
    }
}