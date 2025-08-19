package entidade;

public class Funcionario {

    public String nome;
    public double salario;
    public double imposto;

    public double salarioImposto(){
        return (salario * imposto)/100;
    }
    public double salarioDescontado(){
        return salario - salarioImposto();
    }

}
