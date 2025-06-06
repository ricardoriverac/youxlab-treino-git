package introducao.programacao_Orientada_Objeto.entities;

public class Triangulo {
    // OBS: Tem que ser coerente oque os atributos estão fazendo e os metedos como o exemplo de area.
    public double a;
    public double b;
    public double c;

    public double area(){
        double p = (a + b + c);
        return Math.sqrt(p * (p - a ) * (p - b) * (p - c));
    }
}
