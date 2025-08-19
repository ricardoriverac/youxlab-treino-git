import java.util.Scanner;

public class Funcao {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Entrando com 3 números");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int maior = max(a, b, c);

        showResult(maior);


        sc.close();
    }

    public static int max(int x, int y, int z) {

        int resultado;
        if (x > y && x > z) {
            resultado = x;
        } else if (y > z) {
            resultado = y;
        } else {
            resultado = z;
        }
        return resultado;
    }
        public static void showResult ( int resultadoFuncao){
            System.out.println("maior = "+ resultadoFuncao);

    }
}
