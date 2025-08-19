package entidade;

public class Aluno {
    private String nome;
    private double bim1;
    private double bim2;
    private double bim3;

    public String alunosReprovados() {

        if (bim1 <= 59 && bim2 <= 59 && bim3 <= 59) {
            return "Aluno Reprovado";

        } else {
            return "Você foi aprovado ";
        }
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getBim1() {
        return bim1;
    }

    public void setBim1(double bim1) {
        this.bim1 = bim1;
    }

    public double getBim2() {
        return bim2;
    }

    public void setBim2(double bim2) {
        this.bim2 = bim2;
    }

    public double getBim3() {
        return bim3;
    }

    public void setBim3(double bim3) {
        this.bim3 = bim3;
    }
}


//public String toString(){
//    return Bim1
//            + Bim2
//            + Bim3
//    }
//}
