package introducao.java.exercicios.Estruturas;

import java.util.Locale;
import java.util.Scanner;

public class Exe04 {
    /// Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode
    /// começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int horaini , horafim;
        horaini = sc.nextInt();
        horafim = sc.nextInt();
        int duracao;
        if (horaini < horafim)
            duracao  = horafim - horaini;
        else
            duracao = 24 - horaini - horafim;

        System.out.printf("O jogo durou %d horas" , duracao);
        sc.close();
    }
}
