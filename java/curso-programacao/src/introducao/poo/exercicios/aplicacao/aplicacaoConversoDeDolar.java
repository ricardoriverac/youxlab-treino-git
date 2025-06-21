package introducao.poo.exercicios.aplicacao;

import introducao.poo.exercicios.entities.ConversoDeDolar;

import java.util.Locale;
import java.util.Scanner;

public class aplicacaoConversoDeDolar {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.println("-Entrada de Dolar-");
        System.out.print("Qual é o valor do dolar: ");
        double vdolar = sc.nextDouble();
        System.out.print("Quanto dolares você quer comprar? : ");
        double dolar = sc.nextDouble();
        double resultado = ConversoDeDolar.conversorfordolar(vdolar , dolar);
        System.out.println(resultado);

    }
}
