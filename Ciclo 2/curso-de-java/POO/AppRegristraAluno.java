package POO;

import static POO.RegistraAluno.getQuantidadeAlunos;

public class AppRegristraAluno {
    public static void main(String args[]){
        RegistraAluno q = new RegistraAluno();
        RegistraAluno beto = new RegistraAluno();
        RegistraAluno carlos = new RegistraAluno();

        q.setNome("Ana Machado");
        beto.setNome("Beto Castro");
        carlos.setNome("Carlos Oliveira");

        System.out.println(q.getNome());

        System.out.println("Contador: "+ getQuantidadeAlunos());


    }
}
