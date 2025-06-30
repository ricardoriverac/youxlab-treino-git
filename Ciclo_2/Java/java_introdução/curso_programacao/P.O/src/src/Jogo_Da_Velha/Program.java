package Jogo_Da_Velha;

import java.util.ArrayList;
import java.util.List;

import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String JogadorNumero1, JogadorNumero2;
        List<String> listaVazia = new ArrayList<>(9);

        String EscolhaJogador1, EscolhaJogador2;
        EscolhaJogador2 = "";


        for (int i = 0; i < 9; i++) {
            listaVazia.add(" ");
        }

        System.out.println("Vamos jogar o Jogo da Velha!");

        System.out.print("Qual o nome do primeiro jogador?: ");
        JogadorNumero1 = input.nextLine();
        System.out.print("Você escolhe X ou O: ");
        EscolhaJogador1 = input.nextLine().toUpperCase();


        while (!EscolhaJogador1.equals("X") && !EscolhaJogador1.equals("O")) {
            System.out.print("A opção inserida não é válida\nInsira novamente (X ou O): ");
            EscolhaJogador1 = input.nextLine().toUpperCase();
        }

        if (EscolhaJogador1.equals("X")) {
            EscolhaJogador2 = "O";
        } else if (EscolhaJogador1.equals("O")) {
            EscolhaJogador2 = "X";
        }


        System.out.print("Qual o nome do Segundo jogador?: ");
        JogadorNumero2 = input.nextLine();

        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
        System.out.println("Sejam bem vindos ao jogo\nJogadores: " + JogadorNumero1 + " (" + EscolhaJogador1 + ")" + " | " + JogadorNumero2 + " (" + EscolhaJogador2 + ")");


        System.out.println("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nEm qual casinha você quer jogar?\n\n0|1|2\n3|4|5\n6|7|8\n");

        System.out.print("Jogador 1 - : ");
        int Opçao = input.nextInt();
        listaVazia.set(Opçao, EscolhaJogador1);

        text(listaVazia);

        for (int i = 0; i < 4; i++) {
            System.out.print("Jogador 2 - : ");
            int Opçao2 = input.nextInt();
            listaVazia.set(Opçao2, EscolhaJogador2);
            text(listaVazia);

            if (resultado(listaVazia).equals("X")) {
                System.out.println("Jogador X venceu!");
                break;
            } else if (resultado(listaVazia).equals("O")) {
                System.out.println("Jogador O venceu!");
                break;
            }

            System.out.print("Jogador 1 - : ");
            Opçao = input.nextInt();
            listaVazia.set(Opçao, EscolhaJogador1);
            text(listaVazia);


            if (resultado(listaVazia).equals("X")) {
                System.out.println("Jogador X venceu!");
                break;
            } else if (resultado(listaVazia).equals("O")) {
                System.out.println("Jogador O venceu!");
                break;
            } else if (resultado(listaVazia).equals("V") && i == 3) {
                System.out.println("Deu velha!");
                break;
            }
        }
    }


    static void text(List<String> listaVazia) {
        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nJogo atual:");
        for (int i = 0; i < listaVazia.size(); i++) {
            System.out.print(listaVazia.get(i) + " ");

            if ((i + 1) % 3 == 0) {
                System.out.println();
            }
            System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");

        }
    }



    static String resultado(List<String> listaVazia) {
        if (
                (listaVazia.get(0).equals("X") && listaVazia.get(1).equals("X") && listaVazia.get(2).equals("X")) ||
                        (listaVazia.get(3).equals("X") && listaVazia.get(4).equals("X") && listaVazia.get(5).equals("X")) ||
                        (listaVazia.get(6).equals("X") && listaVazia.get(7).equals("X") && listaVazia.get(8).equals("X")) ||
                        (listaVazia.get(0).equals("X") && listaVazia.get(3).equals("X") && listaVazia.get(6).equals("X")) ||
                        (listaVazia.get(1).equals("X") && listaVazia.get(4).equals("X") && listaVazia.get(7).equals("X")) ||
                        (listaVazia.get(2).equals("X") && listaVazia.get(5).equals("X") && listaVazia.get(8).equals("X")) ||
                        (listaVazia.get(0).equals("X") && listaVazia.get(4).equals("X") && listaVazia.get(8).equals("X")) ||
                        (listaVazia.get(2).equals("X") && listaVazia.get(4).equals("X") && listaVazia.get(6).equals("X"))
        ) {
            return "X";
        } else if (
                (listaVazia.get(0).equals("O") && listaVazia.get(1).equals("O") && listaVazia.get(2).equals("O")) ||
                        (listaVazia.get(3).equals("O") && listaVazia.get(4).equals("O") && listaVazia.get(5).equals("O")) ||
                        (listaVazia.get(6).equals("O") && listaVazia.get(7).equals("O") && listaVazia.get(8).equals("O")) ||
                        (listaVazia.get(0).equals("O") && listaVazia.get(3).equals("O") && listaVazia.get(6).equals("O")) ||
                        (listaVazia.get(1).equals("O") && listaVazia.get(4).equals("O") && listaVazia.get(7).equals("O")) ||
                        (listaVazia.get(2).equals("O") && listaVazia.get(5).equals("O") && listaVazia.get(8).equals("O")) ||
                        (listaVazia.get(0).equals("O") && listaVazia.get(4).equals("O") && listaVazia.get(8).equals("O")) ||
                        (listaVazia.get(2).equals("O") && listaVazia.get(4).equals("O") && listaVazia.get(6).equals("O"))
        ) {
            return "O";
        } else {
            return "V";
        }
    }
}