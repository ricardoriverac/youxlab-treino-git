package aplicacao;

import java.util.ArrayList;

public class Programa {
    public static void main(String[] args) {
        ArrayList<Integer>valores = new ArrayList<Integer>();
        ArrayList<Integer>dobro = new ArrayList<Integer>();
        ArrayList<Integer>par = new ArrayList<Integer>();
        ArrayList<Integer>impar = new ArrayList<Integer>();

        valores.add(1);
        valores.add(2);
        valores.add(3);
        valores.add(4);
        valores.add(5);
        valores.add(6);

        valores.forEach((valor)-> {dobro.add(valor*2);});
//                if(valor%2 == 0) {
//                    par.add(valor);
//                }else {
//                    impar.add(valor);
//                }
//            });
//
//
//        System.out.println(valores);
//        System.out.println(dobro);
//        System.out.println(par);
//        System.out.println(impar);

    }
}
