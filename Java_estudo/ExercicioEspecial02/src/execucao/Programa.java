package execucao;

import entidades.Caminhao;
import entidades.Carro;
import entidades.Moto;
import entidades.Veiculo;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Me diga o nome do veículo: ");
        String nomeVeiculo = sc.nextLine();

        System.out.println("A placa do veículo: ");
        int placa = sc.nextInt();

        sc.nextLine();
        System.out.println("O modelo do veículo.carro/moto ou caminhão ");
        String tipoVeiculo = sc.nextLine();

        System.out.println("Quantidade de dias: ");
        int dias = sc.nextInt();

        System.out.println("Preço por dia: ");
        Double preco=sc.nextDouble();

        sc.nextLine();
        System.out.println("Me diga o ponto X: ");
        String pontoX = sc.nextLine();

        System.out.println("Me diga o ponto Y: ");
        String pontoY = sc.nextLine();


        if(tipoVeiculo.equals("carro")){
            Veiculo carro = new Carro(nomeVeiculo, tipoVeiculo, placa, preco);
            System.out.println("Vai custar ao todo: " + carro.calcularPreco(dias, preco));
            System.out.println(carro.mover(pontoX,pontoY));
        }
        else if (tipoVeiculo.equals("moto")){
            Veiculo moto = new Moto(nomeVeiculo, tipoVeiculo, placa, preco);
            System.out.println("Vai custar ao todo: " + moto.calcularPreco(dias, preco));
            System.out.println(moto.mover(pontoX,pontoY));
        }
        else{
            Veiculo caminhao = new Caminhao(nomeVeiculo, tipoVeiculo, placa, preco);
            System.out.println("Vai custar ao todo: " + caminhao.calcularPreco(dias, preco));
            System.out.println(caminhao.mover(pontoX,pontoY));
        }

    }
}
