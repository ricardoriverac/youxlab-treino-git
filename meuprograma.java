import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class meuprograma{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        List <String> nomes = new ArrayList<>();

        System.out.print("Digite um nome: ");
        String nome = input.next();
        nomes.add(nome);

        System.out.println("Digite outro nome: ");
        String nome2 = input.next();
        nomes.add(nome2);

        int range = input.nextInt();
        for(int i = 0; i < range; i++){
            System.out.println("Digite o nome da " + i + " Pessoa");
            String pessoa = input.next();
            nomes.add(pessoa);

        }

        if (nomes.contains("Bruno")){
            System.out.println("Bruno está na lista");
        }
        System.out.println("Os nomes da lista são: " + nomes + "e possui " + nomes.size() + " Pessoas" );
        for (String nomee : nomes){
            System.out.println(nomee);
        }
        List <Number> nums = new ArrayList<>();
        System.out.println("Adicione numeros a lista");
        System.out.println("Quantos numeros voce quer adicionar? ");
        for (int n = 0; n < range; n++) {
            int num = input.nextInt();
            nums.add(num);
            




        }


        
    }
}

