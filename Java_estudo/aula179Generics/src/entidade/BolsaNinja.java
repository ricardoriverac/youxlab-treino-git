package entidade;

import java.util.ArrayList;
import java.util.List;

public class BolsaNinja <T> {
    //Inicializar nosso Array
    private List<T> ferramentas;

    //Construtor
    public BolsaNinja() {
        this.ferramentas = new ArrayList<>();
    }
    //Colocar ferramentas em Array

    public void adicionarFerramenta(T ferramenta){
        ferramentas.add(ferramenta);
    }
    //Print lista de ferramentas

    public void mostrarFerramenta(){
        for (T ferramenta : ferramentas){
            System.out.println(ferramenta);
        }

    }
}
