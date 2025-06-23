package introducao.poo.exercicios.entities;

public class Empregado {
    public String nome;
    public double salario_bruto;
    public double imposto;

    public double Salariotaxado(){
        return salario_bruto -= imposto;
    }
    public void AumentandoSalario(double porcetagem){
        salario_bruto += (salario_bruto * porcetagem / 100);
    }
    public String toString(){
        return nome
                + ", R$ "
                + salario_bruto;
    }
}
