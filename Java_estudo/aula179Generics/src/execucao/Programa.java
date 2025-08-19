package execucao;

import entidade.BolsaNinja;
import entidade.Kunai;
import entidade.Pergaminho;
import entidade.Shuriken;

public class Programa {
    public static void main(String[] args) {
        BolsaNinja<Object> bolsaNinja = new BolsaNinja<>();

        bolsaNinja.adicionarFerramenta(new Kunai("Kunai explosiva"));
        bolsaNinja.adicionarFerramenta(new Pergaminho("Letras"));
        bolsaNinja.adicionarFerramenta(new Shuriken(3));

        System.out.println("Itens da bolsa: ");
        bolsaNinja.mostrarFerramenta();
    }
}
