import java.util.Scanner;

public class Case {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        String dia;

        switch (x){
            case 1:
                dia ="Segunda";
                break;
            case 2:
                dia = "Terça";
                break;
            case 3:
                dia = "quarta";
                break;
            case 4:
                dia = "Quinta";
                break;
            case 5:
                dia = "Sexta";
            default:
                dia = "Valor digitado inválido";
                break;
        }

        System.out.println("Dia da semana "+ dia);
        sc.close();
    }
}
