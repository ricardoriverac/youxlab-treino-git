package introducao.poo.exercicios.entities;

public class Estudante {
    public String nome;
    public double nota1;
    public double nota2;
    public double nota3;

    public double somadanotas(){
        double soma = nota3 + (nota1 + nota2);
        if (soma > 60){
            System.out.println("Aprovado");
        }
        else{
            double falta = 60 - soma;
            System.out.println("Reprovado");
            System.out.println("Falta: " + falta);
        }
        return soma;
    }
}
