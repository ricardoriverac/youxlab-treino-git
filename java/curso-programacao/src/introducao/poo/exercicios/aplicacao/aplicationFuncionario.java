package introducao.poo.exercicios.aplicacao;

import introducao.poo.exercicios.entities.Funcionario;

import java.util.*;

public class aplicationFuncionario {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        List<Funcionario> list = new ArrayList<>();
        System.out.print("Digite a quantidade de funcionarios: ");
        int quant = input.nextInt();
        for (int i = 0; i < quant; i++) {
            Funcionario funcio = new Funcionario();
            System.out.printf("Funcionario #%d: %n", i + 1);
            System.out.print("Digite o ID: ");
            funcio.setId(input.nextInt());
            for (Funcionario funcionario : list) {
                if (Objects.equals(funcio.getId(), funcionario.getId())) {
                    System.out.println("Digite outro por que ja existe!");
                    while (Objects.equals(funcio.getId(), funcionario.getId())) {
                        System.out.println("Novamente");
                        funcio.setId(input.nextInt());
                    }
                }
            }
            input.nextLine();
            System.out.print("Digite o nome: ");
            funcio.setNome(input.nextLine());
            System.out.print("Digite o salário: ");
            funcio.setSalary(input.nextDouble());
            list.add(funcio);
        }
        System.out.print("Digite o ID do funcionario que terá aumento salarial: ");
        int idDoFuncio = input.nextInt();
        Integer pos = position(list , idDoFuncio);
        if (pos == null){
            System.out.println("Esse id não existe ");
        }
        else {
            System.out.print("Entre com a porcetagem: ");
            double porcetagem = input.nextDouble();
            list.get(pos).aumentoSalario(porcetagem);
        }
        System.out.println("lista atualizada");
        for (Funcionario funcionario : list) {
            System.out.printf("%d , %s , %.2f %n" , funcionario.getId() , funcionario.getNome() , funcionario.getSalary());
        }
    }
    public static Integer position(List<Funcionario> list , int id){
        for (int i = 0; i < list.size(); i++){
            if (list.get(i).getId() == id){
                return i;
            }
        }
        return null;
    }
}
