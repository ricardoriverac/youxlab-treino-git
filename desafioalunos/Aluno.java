package desafioalunos;
import java.util.List;
import java.util.ArrayList;

public class Aluno {
    String nome;
    int matricula;
    List<Double> notas;

    public Aluno(String nome, int matricula, double nota){
        this.nome = nome;
        this.matricula = matricula;
        this.notas = new ArrayList<>();
    }

    Aluno(String nome, int matricula){

        this.nome = nome;
        this.matricula = matricula;
    }


    void adicionarNota(Double nota){
        if(nota >= 0 && nota <= 10){
            notas.add(nota);
        }
        else{
            System.out.println("Digite uma nota entre 0 e 10!");
        }
    }


    public Double calcularMedia(){
        if(notas.isEmpty()) return 0.0;
    
        Double soma = 0.0;

        for(Double nota : notas){
            soma += nota;
        }
        
        return soma / notas.size();

    }

    void mostrarSituacao(){
        Double media = calcularMedia();

        if(media > 7.0){
            System.out.println("Aluno " + nome + " está aprovado! ");
        }

        if (media < 7.0){
            System.out.println("Aluno " + nome + " esta reprovado!");
        }
    }
}
