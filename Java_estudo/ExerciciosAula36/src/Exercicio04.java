import java.util.Scanner;

public class Exercicio04 {
    public static void main(String[] args) {
        //Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode
        //começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
        Scanner sc = new Scanner(System.in);
        double horaInicial = sc.nextInt();
        double horaFinal = sc.nextInt();

        if (horaFinal < horaInicial) {
            System.out.println("Não se passou 1 dia");
        }
         else{
             System.out.println("Passou um dia");
            }





    }
}
