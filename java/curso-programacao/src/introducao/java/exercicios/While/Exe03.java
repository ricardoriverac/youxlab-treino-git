package introducao.java.exercicios.While;

import java.util.Scanner;

public class Exe03 {
    /// <p style= color:purple>Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva
    /// um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel
    /// 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até
    /// que seja válido). O programa será encerrado quando o código informado for o número 4. Deve ser escrito a
    /// mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme
    /// exemplo.</p>
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int alcool = 0;
        int gasolina = 0;
        int diesel = 0;
        System.out.println("-- Bem-Vindo ao posto --");
        System.out.print("Digite 0 para começar ");
        int tipo = sc.nextInt();
        while (tipo != 4) {
            System.out.println("""
                    Qual deseja comprar: \s
                    [1] alcool
                    [2] gasolina
                    [3] diesel
                    [4] sair""");
            System.out.print("Digite a opção: ");
            tipo = sc.nextInt();
            if (tipo != 1 && tipo != 2 && tipo != 3 && tipo != 4){
                System.out.println("Opção Inválida");
            }
            if (tipo == 1) {
                alcool = alcool + 1;
            }
            else if (tipo == 2) {
                gasolina = gasolina + 1;
            }
            else if (tipo == 3) {
                diesel = diesel + 1;
            }
        }
        System.out.println("MUITO OBRIGADO");
        System.out.println("Alcool: " + alcool);
        System.out.println("Gasolina: " + gasolina);
        System.out.println("Diesel: " + diesel);

        sc.close();
    }
}
