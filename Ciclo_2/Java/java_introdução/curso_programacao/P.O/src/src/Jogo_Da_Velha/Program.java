package Jogo_Da_Velha;

import java.util.ArrayList;
import java.util.List;

import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String JogadorNumero1, JogadorNumero2;
        List<String> ListaVazia = new ArrayList<>(9);

        String EscolhaJogador1, EscolhaJogador2;
        EscolhaJogador2 = "";


        for (int i = 0; i < 9; i++) {
            ListaVazia.add(" ");
        }

        List<Integer> ListaPosições = new ArrayList<>(9);

        for (int i = 0; i < 9; i++) {
            ListaPosições.add(i);
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
        System.out.println("Sejam bem vindos ao jogo\nJogadores: " + JogadorNumero1 + "(" + EscolhaJogador1 + ")" + " | " + JogadorNumero2 + "(" + EscolhaJogador2 + ")");


        System.out.println("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nEm qual casinha você quer jogar?\n\n0|1|2\n3|4|5\n6|7|8\n");

        for (int o = 0; o < 8; o++) {

            System.out.print("Jogador 1 - : ");
            int Opçao = input.nextInt();
            ListaVazia.set(Opçao, EscolhaJogador1);
            System.out.println(ListaVazia);

            int Opçao2 = -1;

            System.out.print("Jogador 2 - : ");
            Opçao2 = input.nextInt();

            ListaVazia.set(Opçao2, EscolhaJogador2);
            System.out.println(ListaVazia);
        }
    }
}
