package introducao.poo.exeveiculo.apllication;

import introducao.poo.exeveiculo.entities.Caminhao;
import introducao.poo.exeveiculo.entities.Carro;
import introducao.poo.exeveiculo.entities.Moto;
import introducao.poo.exeveiculo.entities.Veiculo;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class aplicationVeiculo {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        System.out.println("--YouX Drives--");
        System.out.println("""
                Available Vehicles: \
                
                [Carro]\
                [Moto]\
                [Caminhão]""");
        System.out.print("Quantos veículos você vai registrar: ");
        int quant = input.nextInt();

        List<Veiculo> veiculos = new ArrayList<>();

        for (int i = 0; i <quant; i++) {
            System.out.println("""
                    Qual dos veículos deseja alugar: \
                    
                    [1] Carro\
                    
                    [2] Moto\
                    
                    [3] Caminhão""");
            System.out.print("Opção: ");
            int opcao = input.nextInt();
            System.out.printf("Registre o %dº veículo %n" , (i+1));
            System.out.print("Modelo: ");
            input.nextLine();
            String modelo = input.nextLine();
            System.out.print("Placa: ");
            String placa = input.nextLine();
            System.out.print("Preço por día: ");
            double precoPorDia = input.nextDouble();
            if (opcao == 1)
                veiculos.add(new Carro(modelo , placa , precoPorDia));
            else if (opcao == 2) {
                veiculos.add(new Moto(modelo , placa , precoPorDia));
            } else if (opcao == 3) {
                veiculos.add(new Caminhao(modelo , placa , precoPorDia));
            }
            else
                System.out.println("--Opção inválida--");
        }
        double sum = 0.0;
        for (Veiculo veiculo : veiculos) {
            System.out.print("Quantos dias você ficara com " + veiculo.getModelo() +": ");
            int dias = input.nextInt();
            System.out.println("Modelo: " + veiculo.getModelo());
            System.out.println("Placa: " + veiculo.getPlaca());
            System.out.println("Preço por dia: " + String.format("%.2f",veiculo.getPrecoPorDia()));
            System.out.println("Total do aluguel : " + String.format("%.2f",veiculo.calcularPreco(dias)));
            sum += veiculo.calcularPreco(dias);
        }
        System.out.println("Total do aluguel de todos os veículos é: " + String.format("%.2f",sum));
        System.out.println();
        System.out.println("Bo andar com os veículos?");
        for (Veiculo veiculo : veiculos) {
            System.out.println("Quais movimentos você vai fazer com: " + veiculo.getModelo());
            System.out.print("X: ");
            int x = input.nextInt();
            System.out.print("Y: ");
            int y = input.nextInt();
            veiculo.mover(x , y);
        }
    }
}
