package aplicacao;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Diga o tamanho da matriz ");
        int numero = sc.nextInt();

        int [][] matriz = new int [numero] [numero];

        for (int linha = 0; linha < numero;linha++ ){
            for (int coluna = 0; coluna <numero;coluna++){
                matriz [linha] [coluna] = sc.nextInt();
            }
        }

        System.out.println("Minha diagonal: ");
        for (int linha =0;linha<numero;linha++){
            System.out.print(matriz[linha] [linha] + " ");
        }

        int negativos = 0;
        for (int linha=0; linha<numero;linha++){
            for(int coluna =0;coluna <numero; coluna++){
                if (matriz [linha] [coluna] < 0){
                    negativos++;
                }

            }
        }
        System.out.println("Numeros negativos: "+ negativos);
        sc.close();
    }
}
