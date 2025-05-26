package desafioalunos;

public class TesteAluno {
    public static void main(String[] args) {
        Aluno aluno1 = new Aluno("Alice", 12121212);

        aluno1.adicionarNota(10.0);
        aluno1.adicionarNota(9.4);

        aluno1.calcularMedia();

        aluno1.mostrarSituacao();
    }
}
