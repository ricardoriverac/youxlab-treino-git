package execucao;

import entidades.Contribuinte;
import entidades.PessoaFisica;
import entidades.PessoaJuridica;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        List<Contribuinte> list = new ArrayList<>();

        System.out.println("Me diga a quantidade de contribuintes: ");
        int quantidade = sc.nextInt();

        for(int contador = 0;contador <= quantidade;quantidade++){
            System.out.println("Pessoa física ou jurídica:[f/j] ");
            char tipoPessoa = sc.next().charAt(0);

            sc.nextLine();
            System.out.println("Nome: ");
            String nome = sc.nextLine();

            System.out.println("Me diga sua contribuição anual: ");
            Double contribuicao = sc.nextDouble();

            if (tipoPessoa == 'f'){
                System.out.println("Me diga seu gasto com saúde: ");
                Double gastoSaude = sc.nextDouble();
                list.add(new PessoaFisica(nome,contribuicao,gastoSaude));
            }
            else{
                System.out.println("Diga a quantidade de funcionários: ");
                Integer quantidadeFuncionario = sc.nextInt();
                list.add(new PessoaJuridica(nome,contribuicao,quantidadeFuncionario));
            }

        }
        System.out.println();

        for(Contribuinte c: list){
            System.out.println(c.taxa());
        }

    }
}
