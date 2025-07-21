package Seção17.Exercicio.App;// Importa as classes necessárias
// Scanner: para ler dados digitados pelo usuário
// HashSet e Set: para armazenar os códigos dos alunos, sem repetir
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Program {
    public static void main(String[] args) {
        // Cria o scanner para ler dados do teclado
        Scanner sc = new Scanner(System.in);

        // Cria um conjunto (Set) para armazenar os códigos dos alunos
        // Usamos HashSet porque ele não permite valores repetidos
        Set<Integer> alunos = new HashSet<>();

        // ---------- Curso A ----------
        System.out.print("Quantos alunos no curso A? ");
        int n = sc.nextInt(); // Lê quantos alunos estão no curso A
        for (int i = 0; i < n; i++) {
            // Lê o código de cada aluno e adiciona no conjunto
            // Se o mesmo aluno aparecer em outro curso, ele não será contado de novo
            alunos.add(sc.nextInt());
        }

        // ---------- Curso B ----------
        System.out.print("Quantos alunos no curso B? ");
        n = sc.nextInt(); // Lê quantos alunos estão no curso B
        for (int i = 0; i < n; i++) {
            alunos.add(sc.nextInt()); // Adiciona os códigos no mesmo conjunto
        }

        // ---------- Curso C ----------
        System.out.print("Quantos alunos no curso C? ");
        n = sc.nextInt(); // Lê quantos alunos estão no curso C
        for (int i = 0; i < n; i++) {
            alunos.add(sc.nextInt()); // Também adiciona aqui
        }

        // Mostra quantos alunos diferentes o professor tem no total
        // Mesmo que um aluno esteja em vários cursos, ele conta apenas uma vez
        System.out.println("Total de alunos: " + alunos.size());

        // Fecha o scanner (boa prática)
        sc.close();
    }
}
