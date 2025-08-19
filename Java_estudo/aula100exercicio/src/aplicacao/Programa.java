package aplicacao;

import entidade.Funcionario;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Funcionario> listaFuncionario = new ArrayList<Funcionario>();

        System.out.println("Me diga a quantidade de funcionários: ");
        int numero = sc.nextInt();


        for (int contador = 0; contador < numero; contador++) {
            System.out.print("Me diga o nome do funcionário: ");
            sc.nextLine();
            String nomeQueOUsuarioDigitou = sc.nextLine();

            System.out.println("Seu salário: ");
            double salarioQueOUsuarioDigitou = sc.nextDouble();

            Funcionario funcionario = new Funcionario();
            funcionario.setNome(nomeQueOUsuarioDigitou);
            funcionario.setSalario(salarioQueOUsuarioDigitou);
            funcionario.setId(contador);

            listaFuncionario.add(funcionario);

        }
        for (Funcionario funcionario : listaFuncionario) {
            System.out.print("Id: " + funcionario.getId());
            System.out.print("Nome: "+funcionario.getNome());
            System.out.print("Salario: " + funcionario.getSalario());
        }

        System.out.println("Digite o id do funcionário que tera aumento: ");
        int idParaAumento = sc.nextInt();

        Integer posicao = temId(listaFuncionario, idParaAumento);


        if (posicao != null) {
            System.out.println("Digite a porcentagem de aumento: ");
            double porcentagem = sc.nextDouble();
            listaFuncionario.get(posicao).aumentarSalario(porcentagem);
        } else {
            System.out.println("Este id não existe!");
        }

        System.out.println("Lista atualizada dos funcionários:");

        for (Funcionario funcionario : listaFuncionario) {
            System.out.println("ID: " + funcionario.getId() +
                    ", Nome: " + funcionario.getNome() +
                    ", Salário: " + funcionario.getSalario());
        }

        sc.close();
    }

    public static Integer temId(List<Funcionario> listaFuncionario, int idParaAumento) {
        for (int contador = 0; contador < listaFuncionario.size(); contador++) {
            if (listaFuncionario.get(contador).getId() == idParaAumento) {
                return contador;
            }
        }
        return null;
    }
}