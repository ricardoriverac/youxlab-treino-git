package ProblemaExemplo.entities;

public class ex3_entities {

    public String nome;
    public double nota1;
    public double nota2;
    public double nota3;

    public double somaDasnota() {
       return nota1 + nota2 + nota3;
    }

    public double quantosPontosFalta(){
        if (somaDasnota() < 60.0){
            return 60.0 - somaDasnota();
        }
    else {
        return 0.0;
        }
    }
}
