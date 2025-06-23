package introducao.poo.exercicios.entities;

public class Triangulo {
    public double altura;
    public double largura;

    public double area(){
        return altura * largura;
    }
    public double perimetro(){
        return (altura + largura) * 2;
    }
    public double diagonal() {
        return Math.sqrt(largura * largura + altura * altura);
    }
}
