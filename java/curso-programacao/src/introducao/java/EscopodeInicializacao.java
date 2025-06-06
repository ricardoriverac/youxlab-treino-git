package introducao.java;

import java.util.Locale;

public class EscopodeInicializacao {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        double price = 1000;
        double discuint;
        if (price > 1000){
            discuint = price * 0.1;
        }
        else
            discuint = 0;
        System.out.println(price);
    }
}
